# coding=utf-8
import glob
import hashlib
import io
import os
import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory

import nbconvert
import nbformat

from .model import Model


def run(bytes_in):
    myzipfile = zipfile.ZipFile(bytes_in)

    with TemporaryDirectory() as temp_dir:
        """Automatically deletes temp_dir if an error occurs"""
        print('\nCreate temporary folder: ', temp_dir)

        out_formats = ['latex', 'html', 'slides', 'rst', 'markdown']
        out_formats_ext = ['tex', 'html', 'slides.html', 'rst', 'md']

        for file in myzipfile.namelist():
            file_dir = myzipfile.namelist()[0]
            if file == file_dir:
                continue

            elif file.startswith(file_dir):
                to_path = temp_dir
                s = 'Copying {0:s} to {1:s}'.format(file, to_path)
                print(s)
                myzipfile.extract(file, to_path)

        all_nam_files = glob.glob(os.path.join(temp_dir, file_dir, '*.nam')) + \
                        glob.glob(os.path.join(temp_dir, file_dir, '*.NAM'))

        assert len(
            all_nam_files
        ) != 0, "The input zip does not contain a .nam nor a .NAM file."

        assert len(
            all_nam_files) == 1, "The zip can only contain a single name file." + \
                                 "The nam files in the zip are: {0}".format(all_nam_files)

        mp = Model(all_nam_files[-1])
        nb = mp.script_model2nb(use_yapf=False)

        buff = io.BytesIO()
        zip_out = zipfile.ZipFile(buff, 'w')

        ipynb_buff = io.StringIO(nbformat.writes(nb))
        zip_out.writestr('test.ipynb', ipynb_buff.getvalue())

        for out_formats_item, out_formats_ext_item in zip(
                out_formats, out_formats_ext):
            ipynb_buff.seek(0)
            zip_out.writestr('test.' + out_formats_ext_item,
                             nbconvert.export(
                                 nbconvert.get_exporter(out_formats_item),
                                 ipynb_buff)[0])

        ipynb_buff.close()
        zip_out.close()
        print('\nContent of the zipfile:')
        zip_out.printdir()

    return buff


def eval_input(bytes_in):
    myzipfile = zipfile.ZipFile(bytes_in)

    with TemporaryDirectory() as temp_dir:
        for file in myzipfile.namelist():
            file_dir = myzipfile.namelist()[0]
            if file == file_dir:
                continue

            elif file.startswith(file_dir):
                myzipfile.extract(file, temp_dir)

        all_nam_files = glob.glob(os.path.join(temp_dir, file_dir, '*.nam')) + \
                        glob.glob(os.path.join(temp_dir, file_dir, '*.NAM'))

        assert len(
            all_nam_files) == 1, "The zip can only contain a single name file"

        filenames_input = next(
            os.walk(os.path.join(temp_dir, file_dir)), (None, None, []))[2]
        print(filenames_input)

        mp = Model(all_nam_files[-1])

    with TemporaryDirectory() as temp_dir_sane_input, TemporaryDirectory(
    ) as temp_dir_made_input:
        print("""
        
        Start testing the created scripts. By loading the input zip file and directly write the input files to a 
        temporary folder. Then create a script using flopymetascript. Evaluate the script, that writes input files to a 
        second temporary folder. And compare the files in the two folders. 
        
        """)
        print('\nCreate temporary folder to write loaded input files: ',
              temp_dir_sane_input)
        mp.sw.change_model_ws(temp_dir_sane_input)
        mp.sw.write_input()

        _, _, filenames_sane_output = next(
            os.walk(temp_dir_sane_input), (None, None, []))
        print('These files were created directly after loading',
              filenames_sane_output)

        d = {'model_ws': temp_dir_made_input}
        mp.change_all_pack_parameter(d)

        s = mp.script_model2string(
            print_descr=False, width=99, bonus_space=0, use_yapf=False)
        print('about to eval the string')

        try:
            exec(s)
        except:
            print('The generated scripts contain errors and dont run well')

        _, _, filenames_output = next(
            os.walk(temp_dir_made_input), (None, None, []))
        print('\nThese files were just created by our generated script',
              filenames_output)

        f_not_the_same = []
        f_are_the_same = []
        f_function_diff = []

        assert len(filenames_sane_output) == len(
            filenames_output), 'Not enough inputfiles were written'

        for fn in filenames_output:
            try:
                path_out = os.path.join(temp_dir_made_input, fn)
                hash_out = hashlib.md5(open(path_out, 'rb').read()).hexdigest()

                path_sane = os.path.join(temp_dir_sane_input, fn)
                path_sane_odj = Path(path_sane)
                path_sane_alt = glob.glob(
                    os.path.join(temp_dir_sane_input, '*' +
                                 path_sane_odj.suffix))[0]
                path_sane = path_sane_alt
                hash_sane = hashlib.md5(
                    open(path_sane, 'rb').read()).hexdigest()

                if hash_sane != hash_out:
                    f_not_the_same.append(fn)

                    text1_split = open(path_out, 'r').read().splitlines()
                    text2_split = open(path_sane, 'r').read().splitlines()

                    for i, (l1,
                            l2) in enumerate(zip(text1_split, text2_split)):
                        if l1 == l2:
                            continue

                        elif l1[0] == '#' and l2[0] == '#':
                            # comment line
                            continue

                        elif l1.strip() == l2.strip():
                            # An extra space appeared somewhere
                            continue

                        elif l1.split('#')[0].strip() == l2.split('#')[
                            0].strip():
                            # Everything before the comment is the same
                            continue

                        elif l1.split('#')[0].strip() == '-1':
                            """
                            Flopymetascript uses -1 if stressperioddata is the 
                            same as in the previous period.
                            """
                            continue

                        else:
                            f_function_diff.append(fn)
                            print(79 * '#')
                            print(fn)
                            print('The input files start to differ on line ',
                                  str(i + 1), ' (one-based).')
                            print('Directly after load: ', l1)
                            print('Via Flopymetascript: ', l2)
                            break

                else:
                    f_are_the_same.append(fn)

            except:
                # Apparently the extension has changed. Now it becomes
                # impossible to relate and compare the two input files
                print('Unable to compare ', fn)

    f_function_the_same = f_are_the_same + [
        item for item in f_not_the_same if item not in f_function_diff
    ]

    print('\nFiles that are the same:       ', f_are_the_same)
    print('Files that are not the same:   ', f_not_the_same)
    print('Files that function the same:  ', f_function_the_same)
    print('Files that function different: ', f_function_diff)
