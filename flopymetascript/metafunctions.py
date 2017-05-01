# coding=utf-8
import glob
import inspect
import io
import os
import pprint
import textwrap
import zipfile
from collections import OrderedDict as od
from functools import partial
from itertools import chain
from pathlib import Path
from tempfile import TemporaryDirectory

import flopy
import nbconvert
import nbformat
import nbformat as nbf
import numpy as np


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

        assert len(all_nam_files) == 1, "The zip can only contain a single name file"

        mp = Model(all_nam_files[-1])
        nb = mp.script_model2nb()

        buff = io.BytesIO()
        zip_out = zipfile.ZipFile(buff, 'w')

        ipynb_buff = io.StringIO(nbformat.writes(nb))
        zip_out.writestr('test.ipynb', ipynb_buff.getvalue())

        for out_formats_item, out_formats_ext_item in zip(out_formats, out_formats_ext):
            ipynb_buff.seek(0)
            zip_out.writestr('test.' + out_formats_ext_item,
                             nbconvert.export(nbconvert.get_exporter(out_formats_item), ipynb_buff)[0])

        ipynb_buff.close()
        zip_out.close()
        print('\nContent of the zipfile:')
        zip_out.printdir()

    return buff


def get_doc_info(s):
    """
    Is used in load function.
    
    usage:
    s = instance.__doc__
    info = get_doc_info(s)

    for k_info, v_info in info.items():
        if k_info in p:
            typed, description = v_info
            p[k_info].typed = typed
            p[k_info].description = description
    """
    if s:
        p = dict()

        for iss, ss in enumerate(s.splitlines()):
            ss_split = ss.split(' : ')

            if len(ss_split) > 1:
                k = ss_split[0].strip()

                p[k] = od()
                typed = ss_split[1].capitalize()

                text = []
                isss = iss
                while True:
                    isss += 1
                    sss = s.splitlines()[isss].split('        ')

                    if len(sss) > 1:
                        text.append(sss[1])

                    else:
                        break

                description = ' '.join(text).capitalize()
                p[k] = typed, description
        return p
    else:
        return {}


def load_package(instance):
    """
    :param instance: either an instance or a class
    :return:
    """

    omitted_keys = ['self', 'kwargs', 'args', 'xul', 'yul', 'rotation', 'proj4_str', 'start_datetime']
    none_ansd_keys = ['model']

    # retreives the instance parameter using inspect
    params = inspect.signature(instance.__init__).parameters

    #
    s = instance.__doc__
    info = get_doc_info(s)

    # store each parameter in an ordered dict as type Parameter
    p = od()

    for k, v in params.items():

        # skip funny keys
        if k in omitted_keys:
            continue

        # Give None value to certain parameters
        elif k in none_ansd_keys:
            p[k] = Parameter(None)

        # For other parameters create value, either from default
        else:

            # If an instance was passed it has loaded values in __dict__
            if k in instance.__dict__:
                p[k] = Parameter(instance.__getattribute__(k))

            # Otherwise use the default value as value
            else:
                p[k] = Parameter(v.default)

        # Fill the Parameter object with other information from the inspect
        p[k].default = v.default
        p[k].kind = v.kind

        # Add documentation to the parameter
        if k in info:
            typed, description = info[k]
            p[k].typed = typed
            p[k].description = description

    # for k_info, v_info in info.items():
    #     if k_info in p:
    #         typed, description = v_info
    #         p[k_info].typed = typed
    #         p[k_info].description = description

    return p


class Model(object):
    """
    For now at least the following need to be loaded if
    one would like to add any packages from that model
        - mf: dis
        - mt: btn
        - swt: dis
    """

    possible_sw_packages = flopy.seawat.Seawat().mfnam_packages
    possible_sw_packages['flopy.modflow'] = flopy.modflow.Modflow
    possible_sw_packages['flopy.mt3d'] = flopy.mt3d.Mt3dms
    possible_sw_packages['flopy.seawat'] = flopy.seawat.Seawat

    def __init__(self, load_nam='', add_pack=[], load_only=None):
        assert isinstance(add_pack, list)

        for i_pack in self.possible_sw_packages.keys():
            assert i_pack in self.possible_sw_packages.keys()

        if load_nam:
            self.load_nam = Path(load_nam)

            assert self.load_nam.is_file()

            f, model_ws = str(self.load_nam.name), str(self.load_nam.parent)

            self.sw = flopy.seawat.Seawat.load(f, version='seawat', exe_name='swt_v4', verbose=False,
                                               model_ws=model_ws, load_only=load_only)

            packagelist = self.sw.get_package_list()

            self.parameters = od()
            self.packages = od()

            for name in packagelist + add_pack:  # + ['mf', 'mt', 'swt']
                pm = od()
                pm['name'] = name

                pm['class'] = self.possible_sw_packages[name.lower()]
                pm['parent_str'] = inspect.getmodule(pm['class']).__package__

                if name in packagelist and name not in add_pack:
                    pm['loaded'] = True
                    pm['instance'] = self.sw.get_package(name=name)

                else:
                    pm['loaded'] = False
                    pm['instance'] = pm['class'](model=self.sw)

                p = load_package(pm['instance'])

                self.parameters[name] = p
                self.packages[name] = pm

        # sanitize
        self.script_sanitize_ncomp()
        self.script_sanitize_BTN_mfenheriting()
        self.script_sanitize_unwanted_parameters()

    def script_sanitize_modelname(self, name):
        for pack_key, pack_val in self.parameters.items():
            if 'modelname' in pack_val:
                self.parameters[pack_key]['modelname']._value = name

    def get_package_constructor(self, name, use_defaults=False):
        constructor = self.packages[name.upper()]['class']

        p = self.parameters[name]
        keys = p.keys()
        if use_defaults:
            values = [p[k].default for k in keys]
        else:
            values = [p[k].value for k in keys]

        kwargs = dict(zip(keys, values))

        kwargs['model'] = self.sw
        del kwargs['extension']

        return partial(constructor, **kwargs)

    def cat_package_file(self, name):
        """
        Print the content of the package file
        :param name: The package acronym
        """
        path = Path(self.packages[name.upper()]['instance'].fn_path)
        with open(path, 'r') as file:
            s = file.read()

        print('\n'.join([str(path.absolute()),
                         len(str(path.absolute())) * '-',
                         s]))

    def script_kwargs2string(self, name, print_descr=True, width=120, bonus_space=0):
        sout = [v.print_string2(k, width=width, bonus_space=bonus_space) for k, v in self.parameters[name].items()]

        if print_descr:
            descr = [v.print_descr(width=width, bonus_space=bonus_space) for _, v in self.parameters[name].items()]

            # zip the two lists, then flatten them using itertools, then remove empty lines. Empty lines originate from
            # when the docstring has no description for the specific parameter
            out = [i for i in chain(*zip(descr, sout)) if i != '']

            return '\n'.join(out)

        else:
            return '\n'.join(sout)

    def script_constructor2string(self, name, width=120, bonus_space=0):
        initial_indent = ' ' * bonus_space

        k = self.parameters[name].keys()
        kwargs = ', '.join(map(''.join, zip(k, 500 * ['='], k)))

        prelude = name.split('.')[-1].lower() + ' = '
        prelude2 = initial_indent + \
                   prelude + \
                   self.packages[name]['class'].__module__ + '.' + \
                   self.packages[name]['class'].__name__ + \
                   '('

        s = prelude2 + kwargs + ')'

        sout = textwrap.wrap(s, width=width, initial_indent=' ' * bonus_space,
                             subsequent_indent=' ' * (bonus_space + len(prelude2)), break_on_hyphens=False,
                             break_long_words=False)

        return '\n'.join(sout)

    def script_package2string(self, name, print_descr=True, width=120, bonus_space=0):
        kwargs = self.script_kwargs2string(name, print_descr=print_descr, width=width, bonus_space=bonus_space)
        constr = self.script_constructor2string(name, width=width, bonus_space=bonus_space)

        return ''.join([kwargs, '\n\n', constr])

    def script_model2string(self, print_descr=True, width=120, bonus_space=0):
        all_modules = ['flopy.modflow', 'flopy.mt3d', 'flopy.seawat']

        out = [self.import_statements()]

        unique_modules = set([item['parent_str'] for name, item in self.packages.items()])

        for mod in [item for item in all_modules if item in unique_modules]:
            pm = od()
            pm['name'] = mod

            pm['class'] = self.possible_sw_packages[mod]
            pm['parent_str'] = 'flopy'
            pm['loaded'] = False
            pm['instance'] = pm['class']()

            self.packages[mod] = pm
            self.parameters[mod] = load_package(pm['instance'])

            self.script_sanitize_modelname(self.sw.name)

            out.append(self.script_package2string(mod, print_descr=print_descr, width=width,
                                                  bonus_space=bonus_space))

            for name, item in self.packages.items():
                if item['parent_str'] != mod:
                    continue

                self.parameters[name]['model'].value = mod.split('.')[-1].lower()

                out.append(
                    self.script_package2string(name, print_descr=print_descr, width=width, bonus_space=bonus_space))

        out.append(self.write_run_statements())
        return '\n\n####################\n'.join(out)

    def script_model2nb(self, print_descr=True, width=120, bonus_space=0):
        """http://nbviewer.jupyter.org/gist/fperez/9716279"""

        nb = nbf.v4.new_notebook()

        all_modules = ['flopy.modflow', 'flopy.mt3d', 'flopy.seawat']

        out = [nbf.v4.new_markdown_cell(self.intro(self.sw.name)),
               nbf.v4.new_code_cell(self.import_statements())]

        unique_modules = set([item['parent_str'] for name, item in self.packages.items()])

        for module in [item for item in all_modules if item in unique_modules]:
            pm = od()
            pm['name'] = module

            pm['class'] = self.possible_sw_packages[module]
            pm['parent_str'] = 'flopy'
            pm['loaded'] = False
            pm['instance'] = pm['class']()

            self.packages[module] = pm
            self.parameters[module] = load_package(pm['instance'])

            self.script_sanitize_modelname(self.sw.name)

            out.append(nbf.v4.new_markdown_cell('# {0}'.format(module)))
            out.append(nbf.v4.new_code_cell(
                self.script_package2string(module, print_descr=print_descr, width=width, bonus_space=bonus_space)))

            for name, item in self.packages.items():
                if item['parent_str'] != module:
                    continue

                self.parameters[name]['model'].value = module.split('.')[-1].lower()

                out.append(nbf.v4.new_markdown_cell('## {0}'.format(name)))
                out.append(nbf.v4.new_code_cell(
                    self.script_package2string(name, print_descr=print_descr, width=width, bonus_space=bonus_space)))

        out.append(nbf.v4.new_markdown_cell('# Run this thing!'))
        out.append(nbf.v4.new_code_cell(self.write_run_statements()))
        nb['cells'] = out
        return nb

    def write_script_model2string(self, fn='', print_descr=True, width=120, bonus_space=0):
        nb = self.script_model2nb(print_descr=print_descr, width=width, bonus_space=bonus_space)

        with open(fn, 'w') as file:
            nbf.write(nb, file)

    @staticmethod
    def intro(title):
        return '# ' + title + '\n' + \
               'This is a file is written using a pre-release version of the meta-flopy-scripting package\n\n' + \
               'Using flopy version {0}'.format(flopy.__version__)

    @staticmethod
    def import_statements():
        return 'import flopy\n' + \
               'import numpy as np\n' + \
               'from numpy import rec'

    def write_run_statements(self):
        modules = ['flopy.seawat', 'flopy.mt3d', 'flopy.modflow']

        for module in modules:
            if module not in self.parameters:
                continue
            else:
                break

        s = '# {0}.write_input()\n# {0}.run_model()'.format(module.split('.')[-1])

        return s

    def script_sanitize_ncomp(self):
        """
        The user is required to enter a kwarg per parameter per species. When loading from file, the parameters are
        loaded for all species into a single list. Thus the list is split up into separate kwargs

        :return:
        """
        import copy

        if 'BTN' not in self.parameters:
            return

        ncomp = self.parameters['BTN']['ncomp'].value

        if ncomp == 1:
            return

        ncomp_adjusts = [['DSP', 'dmcoef'],
                         ['BTN', 'sconc'],
                         ['RCT', 'sp1'],
                         ['RCT', 'sp2'],
                         ['RCT', 'rc1'],
                         ['RCT', 'rc2'],
                         ['RCT', 'srconc']]

        for adjust_item in ncomp_adjusts:
            name, par_name = adjust_item[0], adjust_item[1]

            if name in self.parameters:
                dmcoef_old = copy.copy(self.parameters[name][par_name])

                for icomp, dmcoef_item in enumerate(dmcoef_old.value):
                    if icomp == 0:
                        key = par_name

                    else:
                        key = par_name + str(icomp + 1)

                    self.parameters[name][key] = Parameter(dmcoef_item)
                    self.parameters[name][key].description = dmcoef_old.description

    def script_sanitize_BTN_mfenheriting(self):
        # Set these variables from the Modflow model (self.parent.mf) unless
        # they are specified in the constructor.
        # self.setmodflowvars(nlay, nrow, ncol, nper, laycon, delr, delc, htop,
        #                     dz, perlen, nstp, tsmult)

        if 'BTN' not in self.parameters:
            return

        del_items = ['nlay', 'nrow', 'ncol', 'nper', 'laycon', 'delr', 'delc', 'htop', 'dz', 'perlen', 'nstp', 'tsmult']

        for key in del_items:
            del self.parameters['BTN'][key]

    def script_sanitize_unwanted_parameters(self):
        unwanted = ['extension', 'unitnumber', 'filenames', 'ftlfree', 'ftlunit', 'MFStyleArr', 'DRYCell',
                    'Legacy99Stor', 'FTLPrint', 'NoWetDryPrint', 'OmitDryBud', 'AltWTSorb']

        for unwanted_item in unwanted:
            for key in self.parameters:
                if unwanted_item in self.parameters[key]:
                    del self.parameters[key][unwanted_item]


class Parameter(object):
    """
    Contains the value in different formats.
    - raw: as was used in the construction of the class
    - value: ndarrays and pure python types. No mflists and flopy-2Darrays
    - compressed: the value is broadcastable to value

    - __get__ returns the value [?]
    """

    def __init__(self, value):
        self.value = value
        self.description = ''
        self.typed = ''
        self.default = ''
        self.kind = ''

    def __repr__(self):
        return self.string

    def __get__(self):
        return self.value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = self.parse_value(value)

    @property
    def compressible(self):
        return self.compressible_fun()

    @property
    def compressed(self):
        return self.compressed_fun()

    @property
    def string(self):
        return self.string_fun(self.value)

    @classmethod
    def parse_value(cls, var):
        if isinstance(var, str):
            value = var
        elif isinstance(var, flopy.seawat.swt.Seawat):
            value = var
        elif isinstance(var, flopy.utils.util_list.MfList):
            value = var.data
        elif isinstance(var, list):
            value = list()
            for ivar in var:
                value.append(Parameter(ivar))
        elif hasattr(var, 'array'):  # flopy 2D and 3D arrays
            value = var.array
        else:
            value = var
        return value

    def compressible_fun(self):
        if isinstance(self.value, dict) and 'k' in self.value[
            0].dtype.names:  # add check for i, j, k keys in dtype of first entry
            compressible, _ = self.parse_mflist(self.value)

        elif isinstance(self.value, dict):
            # OC stressperioddata
            compressible, _ = self.parse_mflist(self.value)

        elif isinstance(self.value, np.ndarray):  # flopy 2D and 3D arrays
            '''
            tries to compress the array. Three compressible options
            -1: unable to reduce in size
            0:  a value in a singleton dimension may be used
            1:  broadcastable array
            '''
            compressible, _ = self.parse_array(self.value)

        elif isinstance(self.value, list):
            compressible, _ = self.parse_list(self.value)

        else:
            compressible, _ = -1, self.value

        return compressible

    def compressed_fun(self):
        if isinstance(self.value, dict) and 0 in self.value and 'k' in self.value[
            0].dtype.names:  # add check for i, j, k keys in dtype of first entry
            _, compressed = self.parse_mflist(self.value)

        elif isinstance(self.value, dict):
            "OC stressperioddata"
            _, compressed = self.parse_mflist(self.value)

        elif isinstance(self.value, np.ndarray):  # flopy 2D and 3D arrays
            '''
            tries to compress the array. Three compressible options
            -1: unable to reduce in size
            0:  a value in a singleton dimension may be used
            1:  broadcastable array
            '''
            _, compressed = self.parse_array(self.value)

        elif isinstance(self.value, list):
            _, compressed = self.parse_list(self.value)

        else:
            _, compressed = -1, self.value

        return compressed

    def string_fun(self, bonus_space=0, max_line_width=np.inf):
        """
        :param max_line_width:
        :param bonus_space:
        :return: Printable string. eval(return) should evaluate to var
        """

        if isinstance(self.value, dict):
            try:
                string = pprint.pformat(self.compressed, indent=bonus_space,
                                        width=max_line_width, compact=True)
            except:
                string = str(self.compressed)

        elif isinstance(self.value, flopy.seawat.swt.Seawat):
            string = 'sw'

        elif isinstance(self.value, np.ndarray):
            string = self.parse_array_str(self.compressed,
                                          self.value.shape,
                                          self.compressible)

        elif isinstance(self.value, list):
            string = self.parse_list_str(self.compressed, self.compressible)

        elif isinstance(self.value, str):
            string = "'" + self.compressed + "'"

        else:
            try:
                string = pprint.pformat(self.value, indent=bonus_space,
                                        width=max_line_width, compact=True)
            except:
                string = str(self.value)

        return string

    @staticmethod
    def parse_list(ar):

        if np.unique([item.value for item in ar]).size == 1:
            return 1, ar
        else:
            return -1, ar

    @staticmethod
    def parse_list_str(ar, compres):
        """
        -1: unable to reduce in size
        1:  broadcastable array

        todo:
        for multiline array strings add extra space in line 2, 3..
        use array2string-prefix for this
        """
        # max_line_width = 80  # might set this to something different later
        # precision = 8
        # suppress_small = True  # to mask some rounding issues

        if compres == -1:
            pre = '['
            post = ']'
            ar_str = ', '.join([item.string for item in ar])
            string = pre + ar_str + post

        elif compres == 1:
            # l = np.unique(ar).size
            if len(ar) == 1:
                string = ar[0].string

            else:
                pre = str(len(ar)) + ' * ['
                post = ']'
                ar_str = ar[0].string
                string = pre + ar_str + post

        return string

    @staticmethod
    def parse_mflist(ar):
        out = {}

        for i, (k, v) in enumerate(sorted(ar.items())):
            if k == 0 or k == (0, 0):
                out[k] = v
            elif k == (-1, -1):
                continue

            elif isinstance(v, list):
                # OC stress period data
                if v != prev:
                    out[k] = v


            elif not isinstance(v, int):  # sometimes there is a placeholder int(0)
                if isinstance(prev, int) or not (prev == v).all():
                    out[k] = v

            prev = v

        if len(out) < len(ar):
            return 1, out
        else:
            return -1, ar

    @staticmethod
    def parse_mflist_str(ar):
        return str(ar)

    def parse_array(self, ar):
        """
        Consolidate an array to something smaller and remains
        broadcastable to the original dimensions. ndim remains the same.

        todo:
        - if squeezable in multiple dimensions, squeeze in all dimensions.
            it currently does this, but the entire most_squeezable_dim can be
            left out.
        :param ar: array to be parsed
        :return: consolidated array
        """
        assert isinstance(ar, np.ndarray)

        output = np.unique(ar)

        if len(output) == 1:
            return 0, output.item()

        else:
            items_per_squeezed_dim = ar.ndim * [0]

            for dim in range(ar.ndim):
                output, index = uniquend(ar, axis=dim, return_index=True)

                if len(index) == 1:
                    items_per_squeezed_dim[dim] = output.size

                else:
                    items_per_squeezed_dim[dim] = ar.size

            most_squeezable_dim = items_per_squeezed_dim.index(min(items_per_squeezed_dim))

            if ar.size == items_per_squeezed_dim[most_squeezable_dim]:
                return -1, ar

            else:
                # can be squeezable in multiple dimensions
                # therefore call self
                cur = uniquend(ar, axis=most_squeezable_dim)

                # test if broadcastable shape, same elements values
                assert np.array_equiv(ar, cur)

                return 1, self.parse_array(cur)[1]

    @staticmethod
    def parse_array_str(ar, orig_shape, compres, precision=8):
        """
        -1: unable to reduce in size
        0:  a value in a singleton dimension may be used
        1:  broadcastable array

        todo:
        for multiline array strings add extra space in line 2, 3..
        use array2string-prefix for this
        """

        max_line_width = np.inf
        suppress_small = True  # to mask some rounding issues
        np.set_printoptions(threshold=np.inf, linewidth=np.inf)

        if compres == 0:
            return str(ar)

        elif compres == -1:
            pre = 'np.array('
            post = ')'
            ar_str = np.array2string(ar, max_line_width=max_line_width,
                                     precision=precision,
                                     suppress_small=suppress_small,
                                     separator=',', prefix=pre)
            ar_str = ' '.join(ar_str.split())
            return pre + ar_str + post

        elif compres == 1:
            pre = 'np.broadcast_to('
            post = ', {0})'.format(orig_shape)
            ar_str = np.array2string(ar, max_line_width=max_line_width,
                                     precision=precision,
                                     suppress_small=suppress_small,
                                     separator=',', prefix=pre)
            ar_str = ' '.join(ar_str.split())
            return pre + ar_str + post

    def value_print_string(self, key, bonus_space=0):
        return "".join([bonus_space * ' ', key, ' = ', self.string])

    def print_string2(self, key, width=120, bonus_space=0):
        prelude = key + ' = '

        if key == 'modflowmodel':
            s = 'modflow'

        elif key == 'mt3dmodel':
            s = 'mt3d'

        elif key == 'model':
            s = self.string[1:-1]

        elif key == 'dtype' and self.string[:15] == '(numpy.record, ':
            # dtype in most packages
            s = "np.dtype(" + self.string[15:]

        elif key == 'dtype' and self.string[:3] == "[('":
            # SSM dtype
            s = "np.dtype(" + self.string + ')'

        else:
            s = self.string

        if key == 'stress_period_data':
            s1 = self.print_string1(s, prelude, width=width - 1, bonus_space=bonus_space)
            s1 = '\\\n'.join(s1)
        else:
            s1 = self.print_string1(s, prelude, width=width, bonus_space=bonus_space)
            s1 = '\n'.join(s1)
        s2 = ' ' * bonus_space + prelude + s1[len(prelude) + bonus_space:]
        return s2

    @staticmethod
    def print_string1(string, prelude, width=120, bonus_space=0):
        """If a value contains a string that contains spaces, it will break"""
        return textwrap.wrap(string, width=width,
                             initial_indent=' ' * (bonus_space + len(prelude)),
                             subsequent_indent=' ' * (bonus_space + len(prelude)), break_on_hyphens=False,
                             break_long_words=False)

    def print_descr(self, width=120, bonus_space=0):
        s = textwrap.fill(self.description, width=width - 2,
                          initial_indent=' ' * bonus_space,
                          subsequent_indent=' ' * (bonus_space + 2),
                          break_on_hyphens=False, break_long_words=False)
        s2 = '\n'.join(['# ' + s1 for s1 in s.splitlines()])
        return s2


def uniquend(ar, return_index=False, return_inverse=False,
             return_counts=False, axis=None):
    # this is becoming a built-in feature in numpy 1.13

    assert isinstance(ar, np.ndarray)

    if axis is None:
        return np.unique(ar, return_index=return_index, return_inverse=return_inverse,
                         return_counts=return_counts)

    ar = np.swapaxes(ar, axis, 0)
    orig_shape, orig_dtype = ar.shape, ar.dtype

    # Must reshape to a contiguous 2D array for this to work...
    ar = ar.reshape(orig_shape[0], -1)
    ar = np.ascontiguousarray(ar)

    dtype = np.dtype((np.void, ar.dtype.itemsize * ar.shape[1]))

    consolidated = ar.view(dtype)

    def reshape_uniq(uniq):
        uniq = uniq.view(orig_dtype)

        uniq = uniq.reshape(-1, *orig_shape[1:])
        uniq = np.swapaxes(uniq, 0, axis)
        return uniq

    output = np.unique(consolidated, return_index,
                       return_inverse, return_counts)

    if not (return_index or return_inverse or return_counts):
        return reshape_uniq(output)
    else:
        uniq = reshape_uniq(output[0])
        return (uniq,) + output[1:]
