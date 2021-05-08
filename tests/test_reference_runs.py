import os

from reference_model_runs.pick_model_runs_fun import fun_test_reference_run

test_example_dir = os.path.abspath("tests/reference_model_runs/MF2005")
mf5_exe = os.path.abspath("tests/mf executables/mf2005")


def test_mf5_ref_run_etsdrt(modelname='etsdrt'):
    fun_test_reference_run(modelname, test_example_dir, mf5_exe)
    pass


# def test_mf5_ref_run_testsfr2(modelname='testsfr2'):
#     fun_test_reference_run(modelname, test_example_dir, mf5_exe)
#     pass


def test_mf5_ref_run_ibs2k(modelname='ibs2k'):
    fun_test_reference_run(modelname, test_example_dir, mf5_exe)
    pass


# def test_mf5_ref_run_l1a2k(modelname='l1a2k'):
#     fun_test_reference_run(modelname, test_example_dir, mf5_exe)
#     pass


def test_mf5_ref_run_twrihfb(modelname='twrihfb'):
    fun_test_reference_run(modelname, test_example_dir, mf5_exe)
    pass


# def test_mf5_ref_run_bcf2ss(modelname='bcf2ss'):
#     fun_test_reference_run(modelname, test_example_dir, mf5_exe)
#     pass


def test_mf5_ref_run_restest(modelname='restest'):
    fun_test_reference_run(modelname, test_example_dir, mf5_exe)
    pass


# def test_mf5_ref_run_str(modelname='str'):
#     fun_test_reference_run(modelname, test_example_dir, mf5_exe)
#     pass


def test_mf5_ref_run_twri(modelname='twri'):
    fun_test_reference_run(modelname, test_example_dir, mf5_exe)
    pass
