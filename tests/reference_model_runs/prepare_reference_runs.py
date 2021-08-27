import glob
import os
from pprint import pformat
from shutil import rmtree, copy2

from pick_model_runs_fun import test_diff_list, load_packages_verbose, run_and_compare_h_cbc
from flopyparser.model import Model

"""This script does three things
1. reorganize the mf5 examples, so that each example has its own folder. Origional input files are placed in inputref.
2. Run the namefile directly from inputdirect folder, without interacting with flopy. Logs are saved to the 
    `report_direct` list.
    Succesful models: etsdrt, l1b2k, testsfr2, ibs2k, l1a2k, twrihfb, bcf2ss, restest, tc2hufv4, twrip, 
3. Load the namefile with flopy. Write the input files to inputflopyload, run mf to write input files to inputflopyload
    and run input files. Logs are saved to the `report_inputflopyload` list.
    Succesful models: etsdrt, l1b2k, testsfr2, ibs2k, l1a2k, twrihfb, bcf2ss, restest, str, twri

4. Create Python script from inputref folder with flopyparser. Run Python script to write input files to 
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
test_example_dir = os.path.abspath("../../tests/reference_model_runs/MF2005")

basenamepaths = sorted(glob.glob(os.path.join(mf_exe_examplerun_dir, '*.nam')))
assert basenamepaths, "Folder empty"

if os.path.exists(test_example_dir):
    rmtree(test_example_dir)

os.mkdir(test_example_dir)

for b in basenamepaths:
    # MF2005
    basename = os.path.basename(b)
    modelname = ''.join(basename.split('.')[:-1])

    # copy model input from exe_folder
    test_model_dir = os.path.join(test_example_dir, modelname)

    test_model_inputref_dir = os.path.join(test_example_dir, modelname, 'inputref')

    test_paths = [test_model_dir, test_model_inputref_dir]

    for test_path in test_paths:
        if os.path.exists(test_path):
            rmtree(test_path)

        os.mkdir(test_path)

    for file in glob.glob(os.path.join(mf_exe_examplerun_dir, modelname + '.*')):
        copy2(file, test_model_inputref_dir)
