from setuptools import setup

setup(name='flopymetascript',
      description='Converts a zip with MODFLOW input files to a zip containing Flopy script',
      version='0.1.0',
      packages=['flopymetascript'],
      license='New BSD',
      author='Bas des Tombe',
      author_email='bdestombe@gmail.com',
      install_requires=['numpy', 'nbformat', 'nbconvert', 'flopy'],
      entry_points={
        "console_scripts": ['flopymetascript = flopymetascript.flopymetascript:main']
        }
      )
