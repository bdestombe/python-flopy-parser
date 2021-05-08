import glob
import os
from pprint import pformat
from shutil import rmtree, copy2

from pick_model_runs_fun import test_diff_list, load_packages_verbose, run_and_compare_h_cbc
from flopymetascript.model import Model

"""This script does three things
1. reorganize the mf5 examples, so that each example has its own folder. Origional input files are placed in inputref.
2. Run the namefile directly from inputdirect folder, without interacting with flopy. Logs are saved to the 
    `report_direct` list.
    Succesful models: etsdrt, l1b2k, testsfr2, ibs2k, l1a2k, twrihfb, bcf2ss, restest, tc2hufv4, twrip, 
3. Load the namefile with flopy. Write the input files to inputflopyload, run mf to write input files to inputflopyload
    and run input files. Logs are saved to the `report_inputflopyload` list.
    Succesful models: etsdrt, l1b2k, testsfr2, ibs2k, l1a2k, twrihfb, bcf2ss, restest, str, twri
    
4. Create Python script from inputref folder with flopymetascript. Run Python script to write input files to 
    inputmetascript
    
Source of test models:
 - MF2005: https://water.usgs.gov/ogw/modflow/MODFLOW-2005_v1.12.00/MF2005.1_12u.zip

Currently all MF2005 examples pass step 2. The following examples fail at step 3:
MNW2-Fig28.nam Does not converge
l1b2k_bath.nam Error in the write routine. [DATA 22 lak1b_bath.txt]
testsfr2_tab.nam [DATA 55  ./../../tests/data/reference_model_runs_old/MF2005/testsfr2_tab/input/testsfr2_tab.tab] not found
                    Should it be an absolut path?

"""

# 1. Create folder structure
mf_exe_examplerun_dir = os.path.abspath("../../scratch/MF2005.1_12u/test-run")
mf_exe_exampleout_dir = os.path.abspath("../../scratch/MF2005.1_12u/test-out")
test_example_dir = os.path.abspath("../../tests/data/reference_model_runs/MF2005")
mf5_exe = os.path.abspath("../../tests/mf executables/mf2005")

basenamepaths = sorted(glob.glob(os.path.join(mf_exe_examplerun_dir, '*.nam')))
assert basenamepaths, "Folder empty"

report = dict()
report_direct = dict()

for b in basenamepaths:
    # MF2005
    basename = os.path.basename(b)
    modelname = ''.join(basename.split('.')[:-1])

    # copy model input from exe_folder
    test_model_dir = os.path.join(test_example_dir, modelname)
    rmtree(test_model_dir)

    test_model_inputref_dir = os.path.join(test_example_dir, modelname, 'inputref')
    test_model_outputref_dir = os.path.join(test_example_dir, modelname, 'outputref')
    test_model_inputdirect_dir = os.path.join(test_example_dir, modelname, 'inputdirect')
    test_model_outputdirect_dir = os.path.join(test_example_dir, modelname, 'outputdirect')
    test_model_inputflopyload_dir = os.path.join(test_example_dir, modelname, 'inputflopyload')
    test_model_outputflopyload_dir = os.path.join(test_example_dir, modelname, 'outputflopyload')
    test_model_inputmetascript_dir = os.path.join(test_example_dir, modelname, 'inputmetascript')
    test_model_outputmetascript_dir = os.path.join(test_example_dir, modelname, 'outputmetascript')

    test_paths = [test_model_dir, test_model_inputref_dir, test_model_inputdirect_dir, test_model_outputref_dir,
                  test_model_outputdirect_dir]

    for test_path in test_paths:
        os.mkdir(test_path)

    for file in glob.glob(os.path.join(mf_exe_examplerun_dir, modelname + '.*')):
        copy2(file, test_model_inputref_dir)

    for file in glob.glob(os.path.join(mf_exe_exampleout_dir, modelname + '.*')):
        copy2(file, test_model_outputref_dir)

# 2. Run the namefile directly from inputdirect folder
basenamepaths = glob.glob(os.path.join(test_example_dir, '*'))

for b in basenamepaths:
    modelname = os.path.basename(b)
    test_model_inputref_dir = os.path.join(b, 'inputref')
    test_model_outputref_dir = os.path.join(b, 'outputref')
    test_model_inputdirect_dir = os.path.join(b, 'inputdirect')
    test_model_outputdirect_dir = os.path.join(b, 'outputdirect')

    for file in glob.glob(os.path.join(test_model_inputref_dir, modelname + '.*')):
        copy2(file, test_model_inputdirect_dir)

    report_direct[modelname] = test_diff_list(modelname, test_model_outputref_dir, test_model_inputdirect_dir,
                                              test_model_outputdirect_dir, mf5_exe)

with open(os.path.join(test_example_dir, '../data', 'MF2005: failed tests step 2.txt'), mode='w') as fh:
    fh.write('Failed models: ' + ', '.join([k for k, v in report_direct.items() if not v['suc']]) + '\n')
    fh.write(
        'Models with diff too large: ' + ', '.join([k for k, v in report_direct.items() if len(v['dif']) > 9]) + '\n')
    fh.write(
        'Diff failed: ' + ', '.join([k for k, v in report_direct.items() if v['dif'][0] == 'Failed to compare']) + '\n')

    for k, v in report_direct.items():
        if not v['suc'] or len(v['dif']) > 9 or v['dif'][0] == 'Failed to compare':
            fh.write(pformat(v, indent=4, width=200) + '\n\n')

suc_model_runs = [k for k, v in report_direct.items() if v['suc'] and len(v['dif']) == 9]

with open(os.path.join(test_example_dir, '../data', 'MF2005: succesful tests step 2.txt'), mode='w') as fh:
    fh.write('Succesful models: ' + ', '.join(suc_model_runs) + '\n')

    for k, v in report_direct.items():
        if v['suc'] and len(v['dif']) == 9:
            fh.write(pformat(v, indent=4, width=200) + '\n\n')

# 3. Load the namefile with flopy
report_flopyload = {}
basenamepaths = [os.path.join(test_example_dir, mn) for mn in suc_model_runs]

for b in basenamepaths:
    modelname = os.path.basename(b)
    test_model_inputref_dir = os.path.join(test_example_dir, modelname, 'inputref')
    test_model_outputref_dir = os.path.join(test_example_dir, modelname, 'outputref')
    test_model_inputdirect_dir = os.path.join(test_example_dir, modelname, 'inputdirect')
    test_model_outputdirect_dir = os.path.join(test_example_dir, modelname, 'outputdirect')
    test_model_inputflopyload_dir = os.path.join(test_example_dir, modelname, 'inputflopyload')
    test_model_outputflopyload_dir = os.path.join(test_example_dir, modelname, 'outputflopyload')

    if os.path.exists(test_model_inputflopyload_dir):
        rmtree(test_model_inputflopyload_dir)

    if os.path.exists(test_model_outputflopyload_dir):
        rmtree(test_model_outputflopyload_dir)

    os.mkdir(test_model_inputflopyload_dir)
    os.mkdir(test_model_outputflopyload_dir)

    fp_nam = os.path.join(test_model_inputref_dir, modelname + '.nam')

    m, report_flopyload[modelname] = load_packages_verbose(fp_nam, test_model_inputref_dir, mf5_exe)
    if not report_flopyload[modelname]['suc']:
        continue

    m, report_flopyload[modelname] = run_and_compare_h_cbc(
        m, test_model_inputdirect_dir, test_model_outputdirect_dir, test_model_inputflopyload_dir,
        test_model_outputflopyload_dir, mf5_exe)
    if not report_flopyload[modelname]['suc']:
        continue

with open(os.path.join(test_example_dir, '../data', 'MF2005: failed tests step 3.txt'), mode='w') as fh:
    fh.write('Failed models: ' + ', '.join([k for k, v in report_direct.items() if not v['suc']]) + '\n')
    for k, v in report_flopyload.items():
        if not v['suc']:
            fh.write(pformat(k, indent=4, width=200) + ': \n')
            fh.write(pformat(v, indent=4, width=200) + '\n\n\n')

suc_model_runs = [k for k, v in report_flopyload.items() if v['suc']]

with open(os.path.join(test_example_dir, '../data', 'MF2005: succesful tests step 3.txt'), mode='w') as fh:
    fh.write('Succesful models: ' + ', '.join(suc_model_runs) + '\n')

    for k, v in report_flopyload.items():
        if v['suc']:
            fh.write(pformat(k, indent=4, width=200) + ': \n')
            fh.write(pformat(v, indent=4, width=200) + '\n\n\n')

# 4. Load the namefile with flopy run flopymetascript and create input files
report_metascript = {}
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

    fp_nam = os.path.join(test_model_inputdirect_dir, modelname + '.nam')
    mp = Model(load_nam=fp_nam)
