import glob
import os
from pprint import pformat
from shutil import rmtree, copy2

from pick_model_runs_fun import test_diff_list, load_packages_verbose, run_and_compare_h_cbc, prepare_model_compare_h_cbc
from flopymetascript.model import Model

modelname = 'etsdrt'
folder = os.path.join('MF2005', modelname)
mf5_exe = os.path.abspath("../../tests/mf executables/mf2005")
test_example_dir = os.path.abspath("../../tests/reference_model_runs/MF2005")

report_metascript = {}
suc_model_runs = ['etsdrt', 'l1b2k', 'testsfr2', 'ibs2k', 'l1a2k', 'twrihfb', 'bcf2ss', 'restest', 'str', 'twri']
basenamepaths = [os.path.join(test_example_dir, mn) for mn in suc_model_runs]

for b in basenamepaths:
    modelname = os.path.basename(b)
    test_model_inputref_dir = os.path.join(test_example_dir, modelname, 'inputref')
    test_model_outputref_dir = os.path.join(test_example_dir, modelname, 'outputref')
    test_model_inputdirect_dir = os.path.join(test_example_dir, modelname, 'inputdirect')
    test_model_outputdirect_dir = os.path.join(test_example_dir, modelname, 'outputdirect')
    test_model_inputflopyload_dir = os.path.join(test_example_dir, modelname, 'inputflopyload')
    test_model_outputflopyload_dir = os.path.join(test_example_dir, modelname, 'outputflopyload')
    test_model_inputmetascript_dir = os.path.join(test_example_dir, modelname, 'inputmetascript')
    test_model_outputmetascript_dir = os.path.join(test_example_dir, modelname, 'outputmetascript')

    if os.path.exists(test_model_inputmetascript_dir):
        rmtree(test_model_inputmetascript_dir)

    if os.path.exists(test_model_outputmetascript_dir):
        rmtree(test_model_outputmetascript_dir)

    os.mkdir(test_model_inputmetascript_dir)
    os.mkdir(test_model_outputmetascript_dir)

    fp_nam = os.path.join(test_model_inputref_dir, modelname + '.nam')

    m, report = load_packages_verbose(fp_nam, test_model_inputref_dir, mf5_exe)
    prepare_model_compare_h_cbc(m)

    m.change_model_ws(test_model_inputflopyload_dir)
    fp_nam = os.path.join(test_model_inputflopyload_dir, modelname + '.nam')

    mp = Model(load_nam=fp_nam)
    mp.change_package_parameter({'flopy.modflow': {'model_ws': test_model_inputmetascript_dir}})

    try:
        s = mp.script_model2string(print_descr=True, width=99)
    except Exception as e:
        print(modelname, "failed: Unable to write the script from the flopymetascript model")
        print(repr(e))
        continue

    try:
        exec(s)
    except Exception as e:
        print(modelname, "Unable to execute the script")
        print(repr(e))
        continue
