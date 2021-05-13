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

from flopymetascript.model import Model


def get_exe_path(exe_name='mf2005'):
    if sys.platform.lower() == "darwin":
        platform = "mac"
        ext = ''
    elif sys.platform.lower().startswith("linux"):
        platform = "linux"
        ext = ''
    elif "win" in sys.platform.lower():
        ext = '.exe'
        is_64bits = sys.maxsize > 2 ** 32
        if is_64bits:
            platform = "win64"
        else:
            platform = "win32"
    else:
        errmsg = (
            "Could not determine platform"
            ".  sys.platform is {}".format(sys.platform)
        )
        raise Exception(errmsg)

    this_fp = os.path.dirname(os.path.abspath(__file__))
    fp = os.path.abspath(os.path.join(this_fp, '..', 'mf executables', platform, exe_name + ext))
    assert os.path.exists(fp), fp + ' Does not exist'
    return fp


def fun_test_reference_run(modelname, test_model_inputref_dir, mf5_exe):
    assert os.path.exists(test_model_inputref_dir), "test_example_dir does not exist"
    # assert os.path.exists(os.path.join(test_example_dir, modelname)), "test_example_dir/modelname does not exist"

    # test_model_inputref_dir = os.path.join(test_example_dir, modelname, 'inputref')

    with tempfile.TemporaryDirectory() as test_model_inputdirect_dir, \
            tempfile.TemporaryDirectory() as test_model_outputdirect_dir, \
            tempfile.TemporaryDirectory() as test_model_inputmetascript_dir, \
            tempfile.TemporaryDirectory() as test_model_outputmetascript_dir:

        # copy reference inputfiles to working dir.
        input_filelist = glob.glob(os.path.join(test_model_inputref_dir, modelname + '*'))
        assert input_filelist, 'Reference run folder: test_example_dir/modelname is empty'

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
        pcks_modified = prepare_model_compare_h_cbc(m)

        for pck in pcks_modified:
            pck.write_file()

        m.write_name_file()

        # Create reference output
        suc, mes = test_inputfiles(modelname, test_model_inputdirect_dir, test_model_outputdirect_dir, mf5_exe)
        assert suc, mes

        # Load reference input files with flopymetascript that also outputs h and cbc.
        fp_nam = os.path.join(test_model_inputdirect_dir, modelname + '.nam')
        mp = Model(load_nam=fp_nam)

        mp.change_package_parameter({'flopy.modflow': {'model_ws': test_model_inputmetascript_dir}})
        # mp.change_package_parameter({'LAK': {'lakarr': test_model_inputmetascript_dir}})
        s = mp.script_model2string(print_descr=False, width=300, use_yapf=False)

        # Run the generated script that writes the inputfiles
        exec(s)

        # Runs the generated input files. And move the output files to the output folder
        suc, mes = test_inputfiles(modelname, test_model_inputmetascript_dir, test_model_outputmetascript_dir, mf5_exe)

        assert suc, mes

        # Compare outputfiles cbc and heads
        hd_fp_ref = os.path.join(test_model_outputdirect_dir, modelname + '.hds')
        hd_fp = os.path.join(test_model_outputmetascript_dir, modelname + '.hds')

        assert test_headfile(hd_fp, hd_fp_ref), 'Heads do not match'

        cbc_fp_ref = os.path.join(test_model_outputdirect_dir, modelname + '.cbc')
        cbc_fp = os.path.join(test_model_outputmetascript_dir, modelname + '.cbc')

        assert test_cbcfile(cbc_fp, cbc_fp_ref), 'Flows do not match'

    pass


def test_inputfiles(modelname, test_model_inputdirect_dir, test_model_outputdirect_dir, mf5_exe):
    """Runs the generated input files. And move the output files to the output folder."""
    input_filelist = glob.glob(os.path.join(test_model_inputdirect_dir, '*'))

    try:
        success, message = run_model(exe_name=mf5_exe, namefile=modelname + '.nam', model_ws=test_model_inputdirect_dir,
                                     silent=True)
    except:
        success = False
        message = 'Failed during run with the generated input files'

    output_filelist = [f for f in glob.glob(os.path.join(test_model_inputdirect_dir, '*')) if f not in input_filelist]
    for file in output_filelist:
        move(file, os.path.join(test_model_outputdirect_dir, os.path.basename(file)))
    return success, message


def test_diff_list(modelname, test_model_outputref_dir, test_model_inputdirect_dir, test_model_outputdirect_dir,
                   mf5_exe):
    success, message = test_inputfiles(modelname, test_model_inputdirect_dir, test_model_outputdirect_dir, mf5_exe)

    # Compare list files
    out_direct_namfp = os.path.join(test_model_outputdirect_dir, modelname + '.lst')
    try:
        # Some reference list files are not readable
        with open(os.path.join(test_model_outputref_dir, modelname + '.lst')) as f_ref:
            file_ref = f_ref.readlines()

        with open(out_direct_namfp) as f_direct:
            file_direct = f_direct.readlines()

        diff = list(
            unified_diff(file_ref, file_direct, modelname + 'reference namefile', modelname + 'direct namefile', n=0))

    except:
        diff = ['Failed to compare']

    pprint({'name': modelname, 'suc': success, 'mes': message, 'dif': diff}, width=200)
    return {'suc': success, 'mes': message, 'dif': diff}


def test_headfile(hd_fp, hd_fp_ref):
    hobj = flopy.utils.HeadFile(hd_fp, precision='auto')
    hobj_ref = flopy.utils.HeadFile(hd_fp_ref, precision='auto')

    h = hobj.get_alldata()
    h_ref = hobj_ref.get_alldata()

    try:
        npt.assert_almost_equal(h, h_ref)
        suc = True
    except:
        suc = False

    return suc


def test_cbcfile(cbc_fp, cbc_fp_ref):
    # cbc1 = flopy.utils.CellBudgetFile(cbc_fp)
    # cbc2 = flopy.utils.CellBudgetFile(cbc_fp_ref)
    cbc_b = open(cbc_fp, mode='rb').read()
    cbc_ref_b = open(cbc_fp_ref, mode='rb').read()

    suc = cbc_ref_b == cbc_b

    return suc


def load_packages_verbose(fp_nam, mf5_exe):
    # m = flopy.modflow.Modflow.load(fp_nam, exe_name=mf5_exe, check=False, verbose=True)
    assert os.path.exists(fp_nam), 'fp_nam does not exist'
    model_ws = os.path.dirname(fp_nam)
    m = flopy.seawat.Seawat.load(
        os.path.basename(fp_nam),
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
        zon = flopy.modflow.ModflowZon.load(os.path.join(model_ws, modelname + '.zon'), m)
        # flopy.modflow.ModflowZon(m, zone_dict=zon)
        # try:
        #     zon = flopy.modflow.ModflowZon.load(os.path.join(test_model_inputref_dir, modelname + '.zon'), m)
        #     flopy.modflow.ModflowZon(m, zone_dict=zon)
        # except Exception as e:
        #     return None, {'suc': False, 'mes': 'Unable to load zones with flopy', 'dif': repr(e)}

    if os.path.exists(os.path.join(model_ws, modelname + '.mlt')):
        mlt = flopy.modflow.ModflowMlt.load(os.path.join(model_ws, modelname + '.mlt'), m)
        # flopy.modflow.ModflowMlt(m, mult_dict=mlt)
        # try:
        #     mlt = flopy.modflow.ModflowMlt.load(os.path.join(test_model_inputref_dir, modelname + '.mlt'), m)
        #     flopy.modflow.ModflowMlt(m, mult_dict=mlt)
        # except Exception as e:
        #     return None, {'suc': False, 'mes': 'Unable to load Mult Package with flopy', 'dif': repr(e)}

    return m, {'suc': True, 'mes': '', 'dif': ''}


def run_and_compare_h_cbc(m, test_model_inputdirect_dir, test_model_outputdirect_dir, test_model_inputflopyload_dir,
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

    test_inputfiles(modelname, test_model_inputdirect_dir, test_model_outputdirect_dir, mf5_exe)
    test_inputfiles(modelname, test_model_inputflopyload_dir, test_model_outputflopyload_dir, mf5_exe)

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


def prepare_model_compare_h_cbc(m):
    # files that need to be adjusted of the reference model as head and cbc are not outputted by default
    fhs = []

    flopy.modflow.mfoc.ModflowOc(model=m, stress_period_data={(0, 0): ['save head', 'save budget']},
                                 unitnumber=[50, 51, 52, 53, 0])
    fhs.append(m.get_package('oc'))

    for p in m.get_package_list():
        if hasattr(m.get_package(p), 'ipakcb'):
            m.get_package(p).ipakcb = 53
            m.add_output_file(53, fname=None, package=p)
            fhs.append(m.get_package(p))

    return fhs
