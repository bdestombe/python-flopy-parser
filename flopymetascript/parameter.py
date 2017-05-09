# coding=utf-8
import pprint
import textwrap

import flopy
import numpy as np
from yapf.yapflib.yapf_api import FormatCode


class Parameter(object):
    """
    Contains the value in different formats.
    - raw: as was used in the construction of the class
    - value: ndarrays and pure python types. No mflists and flopy-2Darrays
    - compressed: the value is broadcastable to value

    - __get__ returns the value [?]
    """

    def __init__(self, value, return_all_data=False):
        self.value = value
        self.description = ''
        self.typed = ''
        self.default = ''
        self.kind = ''
        self.return_all_data = return_all_data

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
        """
        -1: unable to reduce in size
        0:  a value in a singleton dimension may be used
        1:  broadcastable array
        
        If return_all_data then make 1 -> -1 and 0 remains 0
        """
        if self.return_all_data:

            return -(self.compressible_fun() ** 2)

        else:
            return self.compressible_fun()

    @property
    def compressed(self):
        return self.compressed_fun()

    @property
    def string(self):
        return self.string_fun()

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
        if isinstance(
                self.value, dict
        ) and 'k' in self.value[0].dtype.names:  # add check for i, j, k keys in dtype of first entry
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
        # add check for i, j, k keys in dtype of first entry
        if isinstance(
                self.value,
                dict) and 0 in self.value and 'k' in self.value[0].dtype.names:
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
                string = pprint.pformat(
                    self.compressed,
                    indent=bonus_space,
                    width=max_line_width,
                    compact=True)
            except:
                string = str(self.compressed)

        elif isinstance(self.value, flopy.seawat.swt.Seawat):
            string = 'sw'

        elif isinstance(self.value, np.ndarray):
            string = self.parse_array_str(self.compressed, self.value.shape,
                                          self.compressible)

        elif isinstance(self.value, list):
            string = self.parse_list_str(self.compressed, self.compressible)

        elif isinstance(self.value, str):
            string = "'" + self.compressed + "'"

        else:
            try:
                string = pprint.pformat(
                    self.value,
                    indent=bonus_space,
                    width=max_line_width,
                    compact=True)
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

        prev = []

        for i, (k, v) in enumerate(sorted(ar.items())):
            if k == 0 or k == (0, 0):
                out[k] = v

            elif k == (-1, -1):
                continue

            elif isinstance(v, list):
                # OC stress period data
                if v != prev:
                    out[k] = v

            elif not isinstance(v, int):
                # sometimes there is a placeholder int(0)

                if isinstance(prev, int) or not prev == v:
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

        if output.size == 1:
            return 0, output.item()

        elif output.size == 0:
            return -1, output

        else:
            items_per_squeezed_dim = ar.ndim * [0]

            for dim in range(ar.ndim):
                output, index = uniquend(ar, axis=dim, return_index=True)

                if len(index) == 1:
                    items_per_squeezed_dim[dim] = output.size

                else:
                    items_per_squeezed_dim[dim] = ar.size

            most_squeezable_dim = items_per_squeezed_dim.index(
                min(items_per_squeezed_dim))

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
            ar_str = np.array2string(
                np.array(ar),
                max_line_width=max_line_width,
                precision=precision,
                suppress_small=suppress_small,
                separator=',',
                prefix=pre)
            ar_str = ' '.join(ar_str.split())
            return pre + ar_str + post

        elif compres == 1:
            pre = 'np.broadcast_to('
            post = ', {0})'.format(orig_shape)
            ar_str = np.array2string(
                ar,
                max_line_width=max_line_width,
                precision=precision,
                suppress_small=suppress_small,
                separator=',',
                prefix=pre)
            ar_str = ' '.join(ar_str.split())
            return pre + ar_str + post

    def value_print_string(self, key, bonus_space=0):
        return "".join([bonus_space * ' ', key, ' = ', self.string])

    def print_string2(self, key, width=99, bonus_space=0, use_yapf=True):
        style = '{based_on_style: google, indent_width: 4, split_before_named_assigns: False, column_limit: ' + str(
            width) + '}'
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

        if use_yapf:
            # the :-1 removes the extra \n which is added by yapf
            s3 = FormatCode(prelude + s, style_config=style)[0][:-1]

        else:
            if key == 'stress_period_data':
                s1 = self.print_string1(
                    s, prelude, width=width - 1, bonus_space=bonus_space)
                s1 = '\\\n'.join(s1)
            else:
                s1 = self.print_string1(
                    s, prelude, width=width, bonus_space=bonus_space)
                s1 = '\n'.join(s1)
            s3 = ' ' * bonus_space + prelude + s1[len(prelude) + bonus_space:]

        return s3

    @staticmethod
    def print_string1(string, prelude, width=99, bonus_space=0):
        """
        Is only used by print_string2 if yapf is not used. 
        If a value contains a string that contains spaces, it will break
        """
        return textwrap.wrap(
            string,
            width=width,
            initial_indent=' ' * (bonus_space + len(prelude)),
            subsequent_indent=' ' * (bonus_space + len(prelude)),
            break_on_hyphens=False,
            break_long_words=False)

    def print_descr(self, width=99, bonus_space=0):
        s = textwrap.fill(
            self.description,
            width=width - 2,
            initial_indent=' ' * bonus_space,
            subsequent_indent=' ' * (bonus_space + 2),
            break_on_hyphens=False,
            break_long_words=False)
        s2 = '\n'.join(['# ' + s1 for s1 in s.splitlines()])
        return s2


def uniquend(ar,
             return_index=False,
             return_inverse=False,
             return_counts=False,
             axis=None):
    # this is becoming a built-in feature in numpy 1.13

    assert isinstance(ar, np.ndarray)

    if ar.size == 0:
        return ar

    if axis is None:
        return np.unique(
            ar,
            return_index=return_index,
            return_inverse=return_inverse,
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

    output = np.unique(consolidated, return_index, return_inverse,
                       return_counts)

    if not (return_index or return_inverse or return_counts):
        return reshape_uniq(output)
    else:
        uniq = reshape_uniq(output[0])
        return (uniq,) + output[1:]
