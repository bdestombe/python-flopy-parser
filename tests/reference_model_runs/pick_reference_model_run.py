import os

from pick_model_runs_fun import fun_test_reference_run, get_exe_path

this_fp = os.path.dirname(os.path.abspath(__file__))
test_example_dir = os.path.abspath(os.path.join(this_fp, 'MF2005'))
mf5_exe = get_exe_path(exe_name='mf2005')


# def test_mf5_ref_run_bcf2ss(modelname='bcf2ss'):
#     fun_test_reference_run(modelname, test_example_dir, mf5_exe)
#     pass
#
# def test_mf5_ref_run_str(modelname='str'):
#     fun_test_reference_run(modelname, test_example_dir, mf5_exe)
#     pass


fun_test_reference_run('l1a2k', test_example_dir, mf5_exe)
