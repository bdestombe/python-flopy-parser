import os
import flopy
from flopy.mbase import run_model

from pick_model_runs_fun import fun_test_reference_run, get_exe_path

this_fp = os.path.dirname(os.path.abspath(__file__))
test_example_dir = os.path.abspath(os.path.join(this_fp, 'MT3DUSGS', 'CTS1'))


# modelnames = ['cts1_mf', 'cts1_mt']
# mf5_exes = [get_exe_path(exe_name='mf2005'), get_exe_path(exe_name='mt3dusgs')]
# test_hdss = [True, False]
# test_cbcs = [True, False]
# test_ucns = [False, True]
# almost_equals = [False, True]
#
# success, message = run_model(exe_name=get_exe_path(exe_name='mf2005'),
#                              namefile='cts1_mf.nam',
#                              model_ws=test_example_dir,
#                              silent=True)
# flopy.seawat.Seawat.load(
#                 'cts1_mf.nam',
#                 version='seawat',
#                 exe_name='swt_v4',
#                 verbose=True,
#                 model_ws=test_example_dir)

fun_test_reference_run('cts1_mt', test_example_dir, get_exe_path(exe_name='mt3dusgs'), test_hds=True, test_cbc=False, test_ucn=True, almost_equal=True)

