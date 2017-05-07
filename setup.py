# coding=utf-8
import sys

from setuptools import setup

if sys.version_info[0] != 3 or sys.version_info[1] < 4:
    print("""
        This script requires Python version 3.4.
        It contains with statements for file handles.
        
        And it contains TemporaryDirectory from tempfile, 
        which was in introduced in 3.2
        """)
    sys.exit(1)

setup(
    name='flopymetascript',
    description=
    'Converts a zip with MODFLOW input files to a zip containing Flopy script',
    version='0.2.0',
    packages=['flopymetascript'],
    license='New BSD',
    author='Bas des Tombe',
    author_email='bdestombe@gmail.com',
    install_requires=['numpy', 'nbformat', 'nbconvert', 'flopy', 'yapf'],
    entry_points={
        "console_scripts":
            ['flopymetascript = flopymetascript.flopymetascript:main']
    })
