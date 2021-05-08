import glob
import os
from pprint import pformat
from shutil import rmtree, copy2
from flopy.mbase import run_model

from pick_model_runs_fun import test_diff_list, load_packages_verbose, run_and_compare_h_cbc, prepare_model_compare_h_cbc, test_inputfiles
from flopymetascript.model import Model

modelname = 'etsdrt'
folder = os.path.join('MF2005', modelname)
mf5_exe = os.path.abspath("../../tests/mf executables/mf2005")
test_example_dir = os.path.abspath("/MF2005")

report_metascript = {}
suc_model_runs = ['etsdrt', 'l1b2k', 'testsfr2', 'ibs2k', 'l1a2k', 'twrihfb', 'bcf2ss', 'restest', 'str', 'twri']
basenamepaths = [os.path.join(test_example_dir, mn) for mn in suc_model_runs]

for b in ['etsdrt']:  # basenamepaths:
    modelname = os.path.basename(b)
    test_model_inputref_dir = os.path.join(test_example_dir, modelname, 'inputref')
    # test_model_outputref_dir = os.path.join(test_example_dir, modelname, 'outputref')
    test_model_inputdirect_dir = os.path.join(test_example_dir, modelname, 'inputdirect')
    test_model_outputdirect_dir = os.path.join(test_example_dir, modelname, 'outputdirect')
    # test_model_inputflopyload_dir = os.path.join(test_example_dir, modelname, 'inputflopyload')
    # test_model_outputflopyload_dir = os.path.join(test_example_dir, modelname, 'outputflopyload')
    test_model_inputmetascript_dir = os.path.join(test_example_dir, modelname, 'inputmetascript')
    test_model_outputmetascript_dir = os.path.join(test_example_dir, modelname, 'outputmetascript')

    clear_folder = [test_model_inputdirect_dir, test_model_inputdirect_dir,
                    test_model_inputmetascript_dir, test_model_outputmetascript_dir]
    for fp in clear_folder:
        if os.path.exists(fp):
            rmtree(fp)

        os.mkdir(fp)

    # copy reference inputfiles to working dir
    input_filelist = glob.glob(os.path.join(test_model_inputref_dir, modelname + '*'))
    for fp in input_filelist:
        copy2(fp, test_model_inputdirect_dir)

    fp_nam = os.path.join(test_model_inputref_dir, modelname + '.nam')

    m, report = load_packages_verbose(fp_nam, test_model_inputref_dir, mf5_exe)

    # Prepare reference model to compare heads and flow.
    # Change Output-Control params to generate heads and flows to compare.
    pcks_modified = prepare_model_compare_h_cbc(m)

    m.change_model_ws(test_model_inputflopyload_dir)
    fp_nam = os.path.join(test_model_inputflopyload_dir, modelname + '.nam')

    mp = Model(load_nam=fp_nam)

    mp.change_package_parameter({'flopy.modflow': {'model_ws': test_model_inputmetascript_dir}})

    try:
        s = mp.script_model2string(print_descr=True, width=99)
        suc, mes = True, ''

    except Exception as e:
        suc, mes = False, "Unable to write the script from the flopymetascript model"
        print("Report", modelname, "Failed", mes)
        print(repr(e))
        continue

    try:
        exec(s)
        suc, mes = True, ''

    except Exception as e:
        suc, mes = False, "Unable to execute the script"
        print("Report", modelname, "Failed", mes)
        print(repr(e))
        continue



    # Runs the generated input files. And move the output files to the output folder.
    try:
        success, message = run_model(exe_name=mf5_exe, namefile=modelname + '.nam', model_ws=test_model_inputdirect_dir,
                                     silent=True)
    except Exception as e:
        suc, mes = False, 'Failed during run with the generated input files'
        print("Report", modelname, "Failed", suc, mes)
        print(repr(e))
        continue




    assert suc, mes
    print("Report", modelname, "Success", mes)
