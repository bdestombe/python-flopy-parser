import glob
import os
import sys
import tempfile
from difflib import unified_diff
from pprint import pprint
from shutil import move, copy2

import flopy
import numpy.testing as npt
from flopy.mbase import run_model
import numpy as np

from flopyparser.model import Model


def get_exe_path(exe_name='mf2005'):
    if sys.platform.lower() == "darwin":
        platform = "mac"
        ext = ''
    elif sys.platform.lower().startswith("linux"):
        platform = "linux"
        ext = ''
    elif "win" in sys.platform.lower():
        ext = '.exe'
        is_64bits = sys.maxsize > 2**32
        if is_64bits:
            platform = "win64"
        else:
            platform = "win32"
    else:
        errmsg = ("Could not determine platform"
                  ".  sys.platform is {}".format(sys.platform))
        raise Exception(errmsg)

    this_fp = os.path.dirname(os.path.abspath(__file__))
    fp = os.path.abspath(
        os.path.join(this_fp, '..', 'mf executables', platform,
                     exe_name + ext))
    assert os.path.exists(fp), fp + ' Does not exist'
    return fp


def fun_test_reference_run(modelname,
                           test_model_inputref_dir,
                           mf5_exe,
                           test_hds=True,
                           test_cbc=True,
                           test_ucn=True,
                           almost_equal=False):
    assert os.path.exists(
        test_model_inputref_dir), "test_example_dir does not exist"
    # assert os.path.exists(os.path.join(test_example_dir, modelname)), "test_example_dir/modelname does not exist"

    # test_model_inputref_dir = os.path.join(test_example_dir, modelname, 'inputref')

    with tempfile.TemporaryDirectory() as test_model_inputdirect_dir, \
            tempfile.TemporaryDirectory() as test_model_outputdirect_dir, \
            tempfile.TemporaryDirectory() as test_model_inputmetascript_dir, \
            tempfile.TemporaryDirectory() as test_model_outputmetascript_dir:

        # copy reference inputfiles to working dir.
        input_filelist = glob.glob(os.path.join(test_model_inputref_dir, '*'))
        assert input_filelist, 'test_model_inputref_dir is empty:' + test_model_inputref_dir

        for fp in input_filelist:
            copy2(fp, test_model_inputdirect_dir)

        fp_nam = os.path.join(test_model_inputref_dir, modelname + '.nam')

        m, report = load_packages_verbose(fp_nam, mf5_exe)

        # modify only the reference input files to also store heads and cbc
        m.change_model_ws(test_model_inputdirect_dir)

        # Prepare reference model to compare heads and flow.
        # Change Output-Control params to generate heads and flows to compare.
        # Modify only the files that require chages. Therefore copy all input files from reference folder and overwrite
        # what is needed.
        pcks_modified = prepare_model_compare_h_cbc(m,
                                                    save_hds=test_hds,
                                                    save_cbc=test_cbc)

        for pck in pcks_modified:
            pck.write_file()

        m.write_name_file()
        fp_nam_direct = os.path.join(m.model_ws, m.namefile)
        with open(fp_nam_direct) as fh:
            print(''.join(fh.readlines()))

        # Create reference output
        suc, mes = test_inputfiles(modelname, test_model_inputdirect_dir,
                                   test_model_outputdirect_dir, mf5_exe)
        assert suc, mes

        # Load reference input files with flopyparser that also outputs h and cbc.
        fp_nam = os.path.join(test_model_inputdirect_dir, modelname + '.nam')
        mp = Model(load_nam=fp_nam)

        mp.change_package_parameter(
            {'flopy.modflow': {
                'model_ws': test_model_inputmetascript_dir
            }})

        if 'flopy.mt3d' in mp.parameters:
            mp.change_package_parameter(
                {'flopy.mt3d': {
                    'model_ws': test_model_inputmetascript_dir
                }})

        if 'flopy.seawat' in mp.parameters:
            mp.change_package_parameter(
                {'flopy.seawat': {
                    'model_ws': test_model_inputmetascript_dir
                }})

        # mp.change_package_parameter({'LAK': {'lakarr': test_model_inputmetascript_dir}})
        s = mp.script_model2string(print_descr=False,
                                   width=300,
                                   use_yapf=False)

        # Run the generated script that writes the inputfiles
        exec(s)

        # Runs the generated input files. And move the output files to the output folder
        suc, mes = test_inputfiles(modelname, test_model_inputmetascript_dir,
                                   test_model_outputmetascript_dir, mf5_exe)

        assert suc, mes

        if False:
            ls_fp = os.path.join(
                test_model_outputdirect_dir, m.lst.file_name[0]
            )  #  modelname + '.' + m._mf.lst.extension[0])
            ls_fp_ref = os.path.join(
                test_model_outputmetascript_dir, model.lst.file_name[0]
            )  #modelname + '.' + m._mf.lst.extension[0])

            glob.glob(test_model_outputmetascript_dir + '/*')
            test_listfile(ls_fp, ls_fp_ref)

        # Compare outputfiles cbc and heads
        if test_hds:
            hd_fp_ref = os.path.join(test_model_outputdirect_dir,
                                     modelname + '.hds')
            hd_fp = os.path.join(test_model_outputmetascript_dir,
                                 modelname + '.hds')

            assert test_headfile(
                hd_fp, hd_fp_ref,
                almost_equal=almost_equal), 'Heads do not match'

        if test_cbc:
            cbc_fp_ref = os.path.join(test_model_outputdirect_dir,
                                      modelname + '.cbc')
            cbc_fp = os.path.join(test_model_outputmetascript_dir,
                                  modelname + '.cbc')

            assert test_cbcfile(
                cbc_fp, cbc_fp_ref,
                almost_equal=almost_equal), 'Flows do not match'

        if test_ucn:
            assert 'BTN' in mp.parameters, 'No BTN package configured therefore no UCN binary to compare. ' \
                                           'test_unc=False?'
            for i in range(mp.parameters['BTN']['ncomp'].value):
                icomp = i + 1
                ucn_fp_ref = os.path.join(test_model_outputdirect_dir,
                                          'MT3D{0:03d}.UCN'.format(icomp))
                ucn_fp = os.path.join(test_model_outputmetascript_dir,
                                      'MT3D{0:03d}.UCN'.format(icomp))

                assert test_ucnfile(
                    ucn_fp, ucn_fp_ref, model=m, almost_equal=almost_equal
                ), 'Concentrations do not match: MT3D{0:03d}.UCN'.format(icomp)

    pass


def test_inputfiles(modelname, test_model_inputdirect_dir,
                    test_model_outputdirect_dir, mf5_exe):
    """Runs the generated input files. And move the output files to the output folder."""
    input_filelist = glob.glob(os.path.join(test_model_inputdirect_dir, '*'))

    success, message = run_model(exe_name=mf5_exe,
                                 namefile=modelname + '.nam',
                                 model_ws=test_model_inputdirect_dir,
                                 silent=True)
    if not success:
        try:
            with open(
                    os.path.join(test_model_outputdirect_dir,
                                 modelname + '.lst')) as fh:
                print(''.join(fh.readlines()))
        except:
            print('NO LISTFILE')

        assert success, message

    output_filelist = [
        f for f in glob.glob(os.path.join(test_model_inputdirect_dir, '*'))
        if f not in input_filelist
    ]
    for file in output_filelist:
        move(file,
             os.path.join(test_model_outputdirect_dir, os.path.basename(file)))
    return success, message


def test_diff_list(modelname, test_model_outputref_dir,
                   test_model_inputdirect_dir, test_model_outputdirect_dir,
                   mf5_exe):
    success, message = test_inputfiles(modelname, test_model_inputdirect_dir,
                                       test_model_outputdirect_dir, mf5_exe)

    # Compare list files
    out_direct_namfp = os.path.join(test_model_outputdirect_dir,
                                    modelname + '.lst')
    try:
        # Some reference list files are not readable
        with open(os.path.join(test_model_outputref_dir,
                               modelname + '.lst')) as f_ref:
            file_ref = f_ref.readlines()

        with open(out_direct_namfp) as f_direct:
            file_direct = f_direct.readlines()

        diff = list(
            unified_diff(file_ref,
                         file_direct,
                         modelname + 'reference namefile',
                         modelname + 'direct namefile',
                         n=0))

    except:
        diff = ['Failed to compare']

    pprint({
        'name': modelname,
        'suc': success,
        'mes': message,
        'dif': diff
    },
           width=200)
    return {'suc': success, 'mes': message, 'dif': diff}


def test_listfile(ls_fp, ls_fp_ref):
    assert os.path.exists(ls_fp), 'ls_fp does not exist'
    assert os.path.exists(ls_fp_ref), 'ls_fp_ref does not exist'
    try:
        # Some reference list files are not readable
        with open(ls_fp_ref) as f_ref:
            file_ref = f_ref.readlines()

        with open(ls_fp) as f_direct:
            file_direct = f_direct.readlines()

        diff = list(
            unified_diff(file_ref,
                         file_direct,
                         'reference listfile',
                         'direct namefile',
                         n=0))

    except:
        diff = ['Failed to compare']

    return diff


def test_headfile(hd_fp, hd_fp_ref, almost_equal=False):
    assert os.path.exists(hd_fp_ref)
    assert os.path.exists(hd_fp)

    hobj = flopy.utils.HeadFile(hd_fp, precision='auto')
    hobj_ref = flopy.utils.HeadFile(hd_fp_ref, precision='auto')

    h = hobj.get_alldata()
    h_ref = hobj_ref.get_alldata()

    if almost_equal:
        # SEAWAT test file solvers aren't set so strict on the residuals
        npt.assert_almost_equal(h, h_ref, decimal=3)
    else:
        npt.assert_almost_equal(h, h_ref)

    suc = True

    return suc


def test_ucnfile(ucn_fp, ucn_fp_ref, model=None, almost_equal=False):
    ucn_b = open(ucn_fp, mode='rb').read()
    ucn_ref_b = open(ucn_fp_ref, mode='rb').read()

    suc = ucn_ref_b == ucn_b

    if not suc:
        ucn1 = flopy.utils.UcnFile(ucn_fp, model=model)
        ucn2 = flopy.utils.UcnFile(ucn_fp_ref, model=model)
        if almost_equal:
            # SEAWAT test file solvers aren't set so strict on the residuals
            npt.assert_almost_equal(ucn1.get_alldata(),
                                    ucn2.get_alldata(),
                                    decimal=4)
        else:
            npt.assert_almost_equal(ucn1.get_alldata(), ucn2.get_alldata())

        suc = True

    return suc


def test_cbcfile(cbc_fp, cbc_fp_ref, almost_equal=False):
    cbc_b = open(cbc_fp, mode='rb').read()
    cbc_ref_b = open(cbc_fp_ref, mode='rb').read()

    suc = cbc_ref_b == cbc_b

    if not suc:
        cbc1 = flopy.utils.CellBudgetFile(cbc_fp)
        cbc2 = flopy.utils.CellBudgetFile(cbc_fp_ref)
        suc = cbc1.recorddict == cbc2.recorddict

        rec_names = cbc2.get_unique_record_names()

        for name in rec_names:
            q1 = cbc1.get_data(text=name, full3D=True)
            q2 = cbc2.get_data(text=name, full3D=True)
            for q1i, q2i in zip(q1, q2):
                if almost_equal:
                    # SEAWAT test file solvers aren't set so strict on the residuals
                    npt.assert_almost_equal(q1i, q2i, decimal=4)
                else:
                    npt.assert_almost_equal(q1i, q2i)

        suc = True

    return suc


def load_packages_verbose(fp_nam, mf5_exe):
    # m = flopy.modflow.Modflow.load(fp_nam, exe_name=mf5_exe, check=False, verbose=True)
    assert os.path.exists(fp_nam), 'fp_nam does not exist'
    model_ws = os.path.dirname(fp_nam)
    m = flopy.seawat.Seawat.load(os.path.basename(fp_nam),
                                 version='seawat',
                                 exe_name=mf5_exe,
                                 verbose=True,
                                 model_ws=model_ws)
    # try:
    #     m = flopy.modflow.Modflow.load(fp_nam, exe_name=mf5_exe, check=False, verbose=True)
    # except Exception as e:
    #     return None, {'suc': False, 'mes': 'Unable to load', 'dif': repr(e)}

    modelname = m.name

    if os.path.exists(os.path.join(model_ws, modelname + '.zon')):
        zon = flopy.modflow.ModflowZon.load(
            os.path.join(model_ws, modelname + '.zon'), m)
        # flopy.modflow.ModflowZon(m, zone_dict=zon)
        # try:
        #     zon = flopy.modflow.ModflowZon.load(os.path.join(test_model_inputref_dir, modelname + '.zon'), m)
        #     flopy.modflow.ModflowZon(m, zone_dict=zon)
        # except Exception as e:
        #     return None, {'suc': False, 'mes': 'Unable to load zones with flopy', 'dif': repr(e)}

    if os.path.exists(os.path.join(model_ws, modelname + '.mlt')):
        mlt = flopy.modflow.ModflowMlt.load(
            os.path.join(model_ws, modelname + '.mlt'), m)
        # flopy.modflow.ModflowMlt(m, mult_dict=mlt)
        # try:
        #     mlt = flopy.modflow.ModflowMlt.load(os.path.join(test_model_inputref_dir, modelname + '.mlt'), m)
        #     flopy.modflow.ModflowMlt(m, mult_dict=mlt)
        # except Exception as e:
        #     return None, {'suc': False, 'mes': 'Unable to load Mult Package with flopy', 'dif': repr(e)}

    return m, {'suc': True, 'mes': '', 'dif': ''}


def run_and_compare_h_cbc(m, test_model_inputdirect_dir,
                          test_model_outputdirect_dir,
                          test_model_inputflopyload_dir,
                          test_model_outputflopyload_dir, mf5_exe):
    # prepare model to compare heads and flow
    pcks_modified = prepare_model_compare_h_cbc(m)

    # modify the reference input files to also store heads and cbc
    m.change_model_ws(test_model_inputdirect_dir)

    for pck in pcks_modified:
        pck.write_file()

    m.write_name_file()

    # write all input files, incl modified
    m.change_model_ws(test_model_inputflopyload_dir)
    m.write_input()

    # for fn in fns:
    #     copy2(os.path.join(test_model_inputflopyload_dir, fn), os.path.join(test_model_inputdirect_dir, fn))

    modelname = m.name

    test_inputfiles(modelname, test_model_inputdirect_dir,
                    test_model_outputdirect_dir, mf5_exe)
    test_inputfiles(modelname, test_model_inputflopyload_dir,
                    test_model_outputflopyload_dir, mf5_exe)

    hd_fp = os.path.join(test_model_outputflopyload_dir, modelname + '.hds')
    hd_fp_ref = os.path.join(test_model_outputdirect_dir, modelname + '.hds')
    cbc_fp = os.path.join(test_model_outputflopyload_dir, modelname + '.cbc')
    cbc_fp_ref = os.path.join(test_model_outputdirect_dir, modelname + '.cbc')

    if not test_headfile(hd_fp, hd_fp_ref):
        return m, {'suc': False, 'mes': 'Heads do not match', 'dif': ''}

    elif not test_cbcfile(cbc_fp, cbc_fp_ref):
        return m, {'suc': False, 'mes': 'Flows do not match', 'dif': ''}

    else:
        return m, {'suc': True, 'mes': 'Flows and heads match', 'dif': ''}


def prepare_model_compare_h_cbc(m, save_hds=True, save_cbc=True):
    # files that need to be adjusted of the reference model as head and cbc are not outputted by default
    from flopy.modflow import ModflowOc

    spd = []
    if save_hds:
        spd.append('save head')

    if save_cbc:
        spd.append('save budget')

    unrs = [14, 51, 52, 53, 0]

    if 'OC' in m.get_package_list():
        unrs[0] = m.oc.unit_number[0] if m.oc.unit_number else unrs[0]
        unrs[1] = m.oc.iuhead if m.oc.iuhead else unrs[1]
        unrs[2] = m.oc.iuddn if m.oc.iuddn else unrs[2]
        unrs[3] = m.oc.iubud if m.oc.iubud else unrs[3]
        unrs[4] = m.oc.iuibnd if m.oc.iuibnd else unrs[4]

        m.remove_package('OC')

        for i in unrs[1:]:
            m.remove_output(unit=abs(i))

    if 'OC' in m._mf.get_package_list():
        m._mf.remove_package('OC')
        for i in unrs[1:]:
            m._mf.remove_output(unit=abs(i))

    oc = flopy.modflow.mfoc.ModflowOc(model=m,
                                      stress_period_data={(0, 0): spd},
                                      unitnumber=unrs)

    fhs = [oc]

    if save_cbc:
        for p in m.get_package_list():
            if hasattr(m.get_package(p), 'ipakcb'):
                if m.get_package(p)['ipakcb'] != unrs[3]:
                    print(m.get_package(p)['ipakcb'], 'ipakcb ori is', unrs)
                    fhs.append(m.get_package(p))

        oc.reset_budgetunit(budgetunit=unrs[3])

    # Check if unitnumber are used twice
    pointers_in_model = pointers_in_model_fun(m)
    unitnumers_in_model = [i[1] for i in pointers_in_model]

    if len(unitnumers_in_model) != len(set(unitnumers_in_model)):
        next_unit = int(max(unitnumers_in_model)) + 1
        m._mf.set_model_units(iunit0=next_unit)

    assert len(unitnumers_in_model) == len(
        set(unitnumers_in_model)), 'Unit number is used multiple times'

    return fhs


def pointers_in_model_fun(m):
    def add_outp_ext(m):
        l = []

        if m is not None:
            # write the external files
            for b, u, f in zip(m.external_binflag, m.external_units,
                               m.external_fnames):
                if b:
                    l.append((f, u))
            for u, f, b in zip(
                    m.output_units,
                    m.output_fnames,
                    m.output_binflag,
            ):
                if u == 0:
                    continue
                else:
                    l.append((f, u))
        return l

    pointers_in_model = []
    # Write global file entry
    if m.glo is not None:
        if m.glo.unit_number[0] > 0:
            pointers_in_model.append(('glo', m.glo.unit_number[0]))
    pointers_in_model.append((m.lst.name[0], m.lst.unit_number[0]))

    pointers_in_model.extend(add_outp_ext(m))
    pointers_in_model.extend(add_outp_ext(m._mf))
    pointers_in_model.extend(add_outp_ext(m._mt))

    for p in m.packagelist:
        for i in range(len(p.name)):
            if p.unit_number[i] == 0:
                continue
            pointers_in_model.append((p.name[i], p.unit_number[i]))
    return pointers_in_model
