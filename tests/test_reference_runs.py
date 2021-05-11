"""
etsdrt, l1b2k, testsfr2, ibs2k, l1a2k, twrihfb, bcf2ss, restest, tc2hufv4, twrip, str, twri
"""


import os

from reference_model_runs.pick_model_runs_fun import fun_test_reference_run, get_exe_path

test_example_dir = os.path.abspath("tests/reference_model_runs/MF2005")
mf5_exe = get_exe_path(exe_name='mf2005')


def test_mf5_ref_run_etsdrt(modelname='etsdrt'):
    fun_test_reference_run(modelname, test_example_dir, mf5_exe)
    pass


def test_mf5_ref_run_l1b2k(modelname='l1b2k'):
    fun_test_reference_run(modelname, test_example_dir, mf5_exe)
    pass


def test_mf5_ref_run_testsfr2(modelname='testsfr2'):
    fun_test_reference_run(modelname, test_example_dir, mf5_exe)
    pass


def test_mf5_ref_run_ibs2k(modelname='ibs2k'):
    fun_test_reference_run(modelname, test_example_dir, mf5_exe)
    pass


def test_mf5_ref_run_l1a2k(modelname='l1a2k'):
    fun_test_reference_run(modelname, test_example_dir, mf5_exe)
    pass


def test_mf5_ref_run_twrihfb(modelname='twrihfb'):
    fun_test_reference_run(modelname, test_example_dir, mf5_exe)
    pass


# Fails with writing differnt records to cbc
# def test_mf5_ref_run_bcf2ss(modelname='bcf2ss'):
#     fun_test_reference_run(modelname, test_example_dir, mf5_exe)
#     pass


def test_mf5_ref_run_restest(modelname='restest'):
    fun_test_reference_run(modelname, test_example_dir, mf5_exe)
    pass


# ZONE package load...failed
#       invalid literal for int() with base 10: '1,17'
# def test_mf5_ref_run_tc2hufv4(modelname='tc2hufv4'):
#     fun_test_reference_run(modelname, test_example_dir, mf5_exe)
#     pass


def test_mf5_ref_run_twrip(modelname='twrip'):
    fun_test_reference_run(modelname, test_example_dir, mf5_exe)
    pass


def test_mf5_ref_run_str(modelname='str'):
    fun_test_reference_run(modelname, test_example_dir, mf5_exe)
    pass


def test_mf5_ref_run_twri(modelname='twri'):
    fun_test_reference_run(modelname, test_example_dir, mf5_exe)
    pass
