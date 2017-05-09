# coding=utf-8
import sys

from setuptools import setup

from flopymetascript import __version__, __name__, __author__

if sys.version_info[0] != 3 or sys.version_info[1] < 4:
    print("""
        This script requires Python version 3.4.
        It contains with statements for file handles.
        
        And it contains TemporaryDirectory from tempfile, 
        which was in introduced in 3.2
        """)
    sys.exit(1)

try:
    import pypandoc

    long_description = pypandoc.convert('README.md', 'rst')
    long_description = long_description.replace("\r", "")

except OSError as e:
    import io

    # pandoc is not installed, fallback to using raw contents
    with io.open('README.md', encoding="utf-8") as f:
        long_description = f.read()

try:
    from flopymetascript.model import Model
    import io
    import nbformat
    import zipfile
    import nbconvert
    import flopy

    p_list = list(flopy.seawat.Seawat().mfnam_packages.keys())

    mp = Model(add_pack=p_list)

    # with description
    nb = mp.script_model2nb(use_yapf=False)
    ipynb_buff = io.StringIO(nbformat.writes(nb))
    s = nbconvert.export(nbconvert.get_exporter('markdown'), ipynb_buff)[0]

    s = s.replace('\n\n```', '\n\n```python')

    p_list_order = list(mp.packages.keys())
    toc = [
        '* [' + i + '](#' + i.replace('.', '') + ')\n' for i in p_list_order
    ]
    toc = ''.join(toc)

    with open('wiki_default_parameters.md', 'w') as f:
        f.write(toc)
        f.write(s)

    ipynb_buff.close()

    # without discription
    nb = mp.script_model2nb(print_descr=False, use_yapf=False)
    ipynb_buff = io.StringIO(nbformat.writes(nb))
    s = nbconvert.export(nbconvert.get_exporter('markdown'), ipynb_buff)[0]

    s = s.replace('\n\n```', '\n\n```python')

    p_list_order = list(mp.packages.keys())
    toc = [
        '* [' + i + '](#' + i.replace('.', '') + ')\n' for i in p_list_order
    ]
    toc = ''.join(toc)

    with open('wiki_default_parameters_without_description.md', 'w') as f:
        f.write(toc)
        f.write(s)

    ipynb_buff.close()

except OSError as e:
    print('unable to update wiki_default_parameters.md')

setup(
    name=__name__,
    description=
    'Converts a zip with MODFLOW input files to a zip containing Flopy script',
    long_description=long_description,
    version=__version__,
    packages=['flopymetascript'],
    license='MIT',
    author=__author__,
    author_email='bdestombe@gmail.com',
    url='https://github.com/bdestombe/flopymetascript',
    download_url='https://github.com/bdestombe/flopymetascript/archive/' +
                 __version__ + '.tar.gz',
    keywords=['flopy', 'groundwater', 'hydrology'],
    install_requires=[
        'numpy>=1.12', 'nbformat>=4.3', 'nbconvert>=5.1', 'flopy>=3.2', 'yapf'
    ],
    platforms='Windows, Mac OS-X',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        "console_scripts":
            ['flopymetascript = flopymetascript.flopymetascript:main']
    })
