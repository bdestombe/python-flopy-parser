import glob
import os
from difflib import unified_diff
from pprint import pprint
from shutil import move, copy2

import flopy
from flopy.mbase import run_model
import numpy.testing as npt


def test_inputfiles(modelname, test_model_inputdirect_dir, test_model_outputdirect_dir, mf5_exe):
    input_filelist = glob.glob(os.path.join(test_model_inputdirect_dir, '*'))

    try:
        success, message = run_model(exe_name=mf5_exe, namefile=modelname + '.nam', model_ws=test_model_inputdirect_dir,
                                     silent=True)
    except:
        success = False
        message = 'Failed during modelrun'

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
    cbc_b = open(cbc_fp, mode='rb').read()
    cbc_ref_b = open(cbc_fp_ref, mode='rb').read()

    suc = cbc_ref_b == cbc_b

    return suc


def load_packages_verbose(fp_nam, test_model_inputref_dir, mf5_exe):
    try:
        m = flopy.modflow.Modflow.load(fp_nam, exe_name=mf5_exe)
    except Exception as e:
        return None, {'suc': False, 'mes': 'Unable to load', 'dif': repr(e)}

    modelname = m.name

    if os.path.exists(os.path.join(test_model_inputref_dir, modelname + '.zon')):
        try:
            zon = flopy.modflow.ModflowZon.load(os.path.join(test_model_inputref_dir, modelname + '.zon'), m)
            flopy.modflow.ModflowZon(m, zone_dict=zon)
        except Exception as e:
            return None, {'suc': False, 'mes': 'Unable to load zones with flopy', 'dif': repr(e)}

    if os.path.exists(os.path.join(test_model_inputref_dir, modelname + '.mlt')):
        try:
            mlt = flopy.modflow.ModflowMlt.load(os.path.join(test_model_inputref_dir, modelname + '.mlt'), m)
            flopy.modflow.ModflowMlt(m, mult_dict=mlt)
        except Exception as e:
            return None, {'suc': False, 'mes': 'Unable to load Mult Package with flopy', 'dif': repr(e)}

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
    # fns = [modelname + '.oc', modelname + '.nam']

    if m.has_package('lpf'):
        m.lpf.ipakcb = 53
        m.add_output_file(
            53, fname=None, package=flopy.modflow.ModflowLpf._ftype()
        )
        fhs.append(m.get_package('lpf'))
        # fns.append(modelname + '.lpf')
    elif m.has_package('bcf6'):
        m.bcf6.ipakcb = 53
        m.add_output_file(
            53, fname=None, package=flopy.modflow.ModflowBcf._ftype()
        )
        fhs.append(m.get_package('bcf6'))
        # fns.append(modelname + '.bc6')

    return fhs
