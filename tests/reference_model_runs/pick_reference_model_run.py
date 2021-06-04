import os

from pick_model_runs_fun import fun_test_reference_run, get_exe_path

this_fp = os.path.dirname(os.path.abspath(__file__))
test_example_dir = os.path.abspath(os.path.join(this_fp, 'MT3DUSGS', 'CTS1'))
mf5_exe = get_exe_path(exe_name='mt3dusgs')
fun_test_reference_run('cts1_mf', test_example_dir, mf5_exe, test_hds=True, test_cbc=False, test_ucn=True)
