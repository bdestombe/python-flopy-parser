"""Model parsing and script generation for MODFLOW models.

This module contains the core Model class that handles loading MODFLOW models,
extracting parameters, and generating Flopy Python scripts and Jupyter notebooks.
"""

import inspect
import textwrap
from collections import OrderedDict
from functools import partial
from itertools import chain
from pathlib import Path

import flopy
import nbformat as nbf
from yapf.yapflib.yapf_api import FormatCode

from .parameter import Parameter


def get_doc_info(s):
    """Extract parameter information from docstring.

    Parses a docstring to extract parameter type and description information.

    Parameters
    ----------
    s : str
        The docstring to parse

    Returns
    -------
    dict
        Dictionary with parameter names as keys and (type, description) tuples as values

    Notes
    -----
    Used in load function. Should be made staticmethod of Model class.
    """
    if s:
        p = {}

        for iss, ss in enumerate(s.splitlines()):
            ss_split = ss.split(" : ")

            if len(ss_split) > 1:
                k = ss_split[0].strip()

                p[k] = OrderedDict()
                typed = ss_split[1].capitalize()

                text = []
                isss = iss
                while True:
                    isss += 1
                    sss = s.splitlines()[isss].split("        ")

                    if len(sss) > 1:
                        text.append(sss[1])

                    else:
                        break

                description = " ".join(text).capitalize()
                p[k] = typed, description
        return p
    else:
        return {}


def load_package(instance):
    """Load package parameters from a Flopy package instance.

    Extracts parameters from a Flopy package instance using inspection
    and docstring parsing.

    Parameters
    ----------
    instance : object
        Flopy package instance to extract parameters from

    Returns
    -------
    collections.OrderedDict
        Ordered dictionary of Parameter objects keyed by parameter name
    """
    omitted_keys = [
        "self",
        "kwargs",
        "args",
        "xul",
        "yul",
        "rotation",
        "proj4_str",
        "start_datetime",
    ]
    none_ansd_keys = ["model"]

    # retreives the instance parameter using inspect
    params = inspect.signature(instance.__init__).parameters

    # Obtain a dictionary with parameter info
    s = instance.__doc__
    info = get_doc_info(s)

    # store each parameter in an ordered dict as type Parameter
    p = OrderedDict()

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

    return p


class Model:
    """MODFLOW model parser and script generator.

    This class handles loading MODFLOW models from name files, extracting
    package parameters, and generating corresponding Flopy Python scripts
    and Jupyter notebooks.

    Notes
    -----
    The following packages need to be loaded for adding other packages:
        - mf: dis (discretization)
        - mt: btn (basic transport)
        - swt: dis (discretization)
    """

    possible_sw_packages = flopy.seawat.Seawat().mfnam_packages
    possible_sw_packages["flopy.modflow"] = flopy.modflow.Modflow
    possible_sw_packages["flopy.mt3d"] = flopy.mt3d.Mt3dms
    possible_sw_packages["flopy.seawat"] = flopy.seawat.Seawat

    def __init__(self, load_nam="", add_pack=None, load_only=None):
        """Initialize Model instance.

        Parameters
        ----------
        load_nam : str, optional
            Path to MODFLOW name file to load
        add_pack : list, optional
            List of additional package names to include
        load_only : list, optional
            List of specific packages to load (others ignored)
        """
        if add_pack is None:
            add_pack = []
        add_pack = list(add_pack)
        assert isinstance(add_pack, list), repr(add_pack)

        for i_pack in add_pack:
            assert i_pack in self.possible_sw_packages.keys()

        if load_nam:
            self.load_nam = Path(load_nam)

            assert self.load_nam.is_file(), "The passed nam file doesnt exist anymore"

            f, model_ws = str(self.load_nam.name), str(self.load_nam.parent)

            self.sw = flopy.seawat.Seawat.load(
                f,
                version="seawat",
                exe_name="swt_v4",
                verbose=False,
                model_ws=model_ws,
                load_only=load_only,
            )

            assert self.sw, f"Could not load namefile {f}"
            # assert self.sw.load_fail is False  # Doesnt work for seawat

            self.sw.array_free_format = True
            bas = self.sw.get_package("BAS6")

            # if bas:
            bas.ifrefm = True
            packagelist = self.sw.get_package_list()
        else:
            self.sw = flopy.seawat.Seawat()
            packagelist = self.sw.get_package_list()

        # All loaded packages
        packagelist += add_pack

        if not packagelist:
            OSError("Noting to do")

        loaded_parameters = OrderedDict()
        loaded_packages = OrderedDict()

        for name in packagelist:
            pm = OrderedDict()
            pm["name"] = name

            pm["class"] = self.possible_sw_packages[name.lower()]
            pm["parent_str"] = inspect.getmodule(pm["class"]).__package__

            if name in packagelist and name not in add_pack:
                # if in add_pack the default will be used
                pm["loaded"] = True
                pm["instance"] = self.sw.get_package(name=name)

            else:
                pm["loaded"] = False

                try:
                    pm["instance"] = pm["class"](model=self.sw)

                except Exception:
                    print(f"{name} Doesnt initiate using loaded or default values")
                    pm["instance"] = pm["class"]
                    # continue

            try:
                p = load_package(pm["instance"])

                loaded_parameters[name] = p
                loaded_packages[name] = pm

            except Exception:
                print(f"{name} failed to load")
                continue

        # Order and include 'flopy.modflow', 'flopy.mt3d', 'flopy.seawat'
        self.parameters = OrderedDict()
        self.packages = OrderedDict()

        all_modules = ["flopy.modflow", "flopy.mt3d", "flopy.seawat"]
        unique_modules = {item["parent_str"] for name, item in loaded_packages.items()}

        if "flopy.mt3d" in unique_modules and "flopy.seawat" not in unique_modules:
            # mt3d requires a seperate mf and mt3d run

            for mod in [item for item in all_modules if item in unique_modules]:
                pm = OrderedDict()
                pm["name"] = mod

                pm["class"] = self.possible_sw_packages[mod]
                pm["parent_str"] = "flopy"
                pm["loaded"] = False
                pm["instance"] = pm["class"]()

                self.packages[mod] = pm
                self.parameters[mod] = load_package(pm["instance"])

                for name, _item in loaded_packages.items():
                    assert name in loaded_parameters, "Each loaded package should have a loaded self.parameters"

                    if loaded_packages[name]["parent_str"] != mod:
                        continue

                    self.packages[name] = loaded_packages[name]
                    self.parameters[name] = loaded_parameters[name]

        else:
            # a single main_model to attach the packages to
            if "flopy.seawat" in unique_modules:
                main_model = "flopy.seawat"

            elif "flopy.mt3d" in unique_modules:
                main_model = "flopy.mt3d"

            else:
                main_model = "flopy.modflow"

            pm = OrderedDict()
            pm["name"] = main_model

            pm["class"] = self.possible_sw_packages[main_model]
            pm["parent_str"] = "flopy"
            pm["loaded"] = False
            pm["instance"] = pm["class"]()

            self.packages[main_model] = pm
            self.parameters[main_model] = load_package(pm["instance"])

            for mod in [item for item in all_modules if item in unique_modules]:
                for name, _item in loaded_packages.items():
                    assert name in loaded_parameters, "Each loaded package should have a loaded self.parameters"

                    if loaded_packages[name]["parent_str"] != mod:
                        continue

                    self.packages[name] = loaded_packages[name]
                    self.parameters[name] = loaded_parameters[name]

            # sanitize
            self.script_sanitize_parentmodel(main_model)

        self.script_sanitize_ncomp()
        self.script_sanitize_btn_mfenheriting()
        self.script_sanitize_unwanted_parameters()
        self.script_sanitize_return_all_data()
        # self.script_sanitize_ensure_2d()git remote set-url origin git@github.com:someuser/newprojectname.git

    def script_sanitize_parentmodel(self, main_model):
        parent = main_model.split(".")[1]

        for p, v in self.parameters.items():
            # if 'model' in v:
            #     v['model'].value = v['parent_str'].split('.')[-1].lower()

            if "model" in v:
                v["model"].value = parent

            if "modflowmodel" in v:
                # in flopy.mt3d and flopy.seawat
                del v["modflowmodel"]

            if "mt3dmodel" in self.parameters[p]:
                # in flopy.seawat
                del v["mt3dmodel"]

    def script_sanitize_modelname(self, name):
        for pack_key, pack_val in self.parameters.items():
            if "modelname" in pack_val:
                self.parameters[pack_key]["modelname"].value = name

    def get_package_constructor(self, name, use_defaults=False):
        """Get package constructor with loaded parameters.

        Parameters
        ----------
        name : str
            Package name
        use_defaults : bool, optional
            Whether to use default values instead of loaded values

        Returns
        -------
        functools.partial
            Partial function for constructing the package
        """
        constructor = self.packages[name.upper()]["class"]

        p = self.parameters[name]
        keys = p.keys()
        if use_defaults:
            values = [p[k].default for k in keys]
        else:
            values = [p[k].value for k in keys]

        kwargs = dict(zip(keys, values, strict=False))

        kwargs["model"] = self.sw
        del kwargs["extension"]

        return partial(constructor, **kwargs)

    def cat_package_file(self, name):
        """Print the content of the package file.

        Parameters
        ----------
        name : str
            The package acronym
        """
        path = Path(self.packages[name.upper()]["instance"].fn_path)
        with open(path) as file:
            s = file.read()

        print("\n".join([str(path.absolute()), len(str(path.absolute())) * "-", s]))

    def script_kwargs2string(self, name, print_descr=True, width=99, bonus_space=0, use_yapf=True):
        sout = [
            v.print_string2(k, width=width, bonus_space=bonus_space, use_yapf=use_yapf)
            for k, v in self.parameters[name].items()
        ]

        if print_descr:
            descr = [v.print_descr(width=width, bonus_space=bonus_space) for _, v in self.parameters[name].items()]

            # zip the two lists, then flatten them using itertools, then remove empty lines. Empty lines originate from
            # when the docstring has no description for the specific parameter
            out = [i for i in chain(*zip(descr, sout, strict=False)) if i != ""]

            return "\n".join(out)

        else:
            return "\n".join(sout)

    def script_constructor2string(self, name, width=99, bonus_space=0, use_yapf=True):
        style = (
            "{based_on_style: google, indent_width: 4, split_before_named_assigns: False, column_limit: "
            + str(width)
            + ", SPLIT_ARGUMENTS_WHEN_COMMA_TERMINATED:True}"
        )

        initial_indent = " " * bonus_space

        k = self.parameters[name].keys()
        kwargs = ", ".join(map("".join, zip(k, 500 * ["="], k, strict=False)))

        prelude = name.split(".")[-1].lower() + " = "
        prelude2 = (
            initial_indent
            + prelude
            + self.packages[name]["class"].__module__
            + "."
            + self.packages[name]["class"].__name__
            + "("
        )

        s = prelude2 + kwargs + ")"

        if use_yapf:
            s2 = FormatCode(s, style_config=style)[0][:-1]

        else:
            sout = textwrap.wrap(
                s,
                width=width,
                initial_indent=" " * bonus_space,
                subsequent_indent=" " * (bonus_space + len(prelude2)),
                break_on_hyphens=False,
                break_long_words=False,
            )
            s2 = "\n".join(sout)

        return s2

    def script_package2string(self, name, print_descr=True, width=99, bonus_space=0, use_yapf=True):
        kwargs = self.script_kwargs2string(
            name,
            print_descr=print_descr,
            width=width,
            bonus_space=bonus_space,
            use_yapf=use_yapf,
        )
        constr = self.script_constructor2string(name, width=width, bonus_space=bonus_space, use_yapf=use_yapf)

        return "".join([kwargs, "\n\n", constr])

    def script_model2string(self, print_descr=True, width=99, bonus_space=0, use_yapf=True):
        self.script_sanitize_modelname(self.sw.name)

        out = [self.import_statements()]

        for name in self.packages:
            out.append(
                self.script_package2string(
                    name,
                    print_descr=print_descr,
                    width=width,
                    bonus_space=bonus_space,
                    use_yapf=use_yapf,
                )
            )

        out.append(self.write_run_statements())
        return "\n\n####################\n".join(out)

    def script_model2nb(self, print_descr=True, width=99, bonus_space=0, use_yapf=True):
        """http://nbviewer.jupyter.org/gist/fperez/9716279"""
        self.script_sanitize_modelname(self.sw.name)

        nb = nbf.v4.new_notebook()

        out = [
            nbf.v4.new_markdown_cell(self.intro(self.sw.name)),
            nbf.v4.new_code_cell(self.import_statements()),
        ]

        for name, _item in self.packages.items():
            out.append(nbf.v4.new_markdown_cell(f"## {name}"))
            out.append(
                nbf.v4.new_code_cell(
                    self.script_package2string(
                        name,
                        print_descr=print_descr,
                        width=width,
                        bonus_space=bonus_space,
                        use_yapf=use_yapf,
                    )
                )
            )

        out.append(nbf.v4.new_markdown_cell("# Run this thing!"))
        out.append(nbf.v4.new_code_cell(self.write_run_statements()))
        nb["cells"] = out
        return nb

    def write_script_model2string(self, fn="", print_descr=True, width=99, bonus_space=0, use_yapf=True):
        nb = self.script_model2nb(
            print_descr=print_descr,
            width=width,
            bonus_space=bonus_space,
            use_yapf=use_yapf,
        )

        with open(fn, "w") as file:
            nbf.write(nb, file)

    @staticmethod
    def intro(title):
        return (
            "# "
            + title
            + "\n"
            + "This is a file is written using a pre-release version of the meta-flopy-scripting package\n\n"
            + f"Using flopy version {flopy.__version__}"
        )

    @staticmethod
    def import_statements():
        return "import flopy\n" + "import numpy as np\n" + "from numpy import rec"

    def write_run_statements(self, write_input=True, run_model=False):
        modules = ["flopy.seawat", "flopy.mt3d", "flopy.modflow"]

        for modules_item in modules:
            if modules_item not in self.parameters:
                continue
            else:
                break

        s1_ = "{}.write_input()".format(modules_item.split(".")[-1])
        s2_ = "{}.run_model()".format(modules_item.split(".")[-1])

        if write_input:
            s1 = s1_

        else:
            s1 = "# " + s1_

        if run_model:
            s2 = s2_

        else:
            s2 = "# " + s2_

        return "\n".join((s1, s2))

    def script_sanitize_ncomp(self):
        """Sanitize multi-component transport parameters.

        The user is required to enter a kwarg per parameter per species.
        When loading from file, the parameters are loaded for all species
        into a single list. This method splits the list up into separate kwargs.
        """
        import copy

        if "BTN" not in self.parameters:
            return

        ncomp_adjusts = [
            ["DSP", "dmcoef"],
            ["BTN", "sconc"],
            ["RCT", "sp1"],
            ["RCT", "sp2"],
            ["RCT", "rc1"],
            ["RCT", "rc2"],
            ["RCT", "srconc"],
        ]

        for name, par_name in ncomp_adjusts:
            if name in self.parameters:
                dmcoef_old = copy.copy(self.parameters[name][par_name])

                for icomp, dmcoef_item in enumerate(dmcoef_old.value):
                    if icomp == 0:
                        key = par_name

                    else:
                        key = par_name + str(icomp + 1)

                    if par_name == "dmcoef" and dmcoef_item.value.ndim == 1 and dmcoef_item.value.size > 1:
                        int(self.parameters["BTN"]["nlay"].value)
                        dmcoef_item.value = dmcoef_item.value[:, None]

                    self.parameters[name][key] = Parameter(dmcoef_item)
                    self.parameters[name][key].description = dmcoef_old.description

    def script_sanitize_btn_mfenheriting(self):
        # Set these variables from the Modflow model (self.parent.mf) unless
        # they are specified in the constructor.
        # self.setmodflowvars(nlay, nrow, ncol, nper, laycon, delr, delc, htop,
        #                     dz, perlen, nstp, tsmult)

        if "BTN" not in self.parameters:
            return

        del_items = [
            "nlay",
            "nrow",
            "ncol",
            "nper",
            "laycon",
            "delr",
            "delc",
            "htop",
            "dz",
            "perlen",
            "nstp",
            "tsmult",
        ]

        for key in del_items:
            del self.parameters["BTN"][key]

    def change_package_parameter(self, d):
        """Change parameters for specific packages.

        Parameters
        ----------
        d : dict
            Nested dictionary with structure {package_name: {key_name: value}}
        """
        for pack_name_item, pack_val_item in d.items():
            for key_name_item, key_val_item in pack_val_item.items():
                # Does the package exists?
                # Does that package contains the required key?
                # assert isinstance(self.parameters[pack_name_item][key_name_item], Parameter)

                # Activates the setter of the Parameter.value
                if pack_name_item in self.parameters:
                    self.parameters[pack_name_item][key_name_item].value = key_val_item

    def change_all_pack_parameter(self, d):
        """Change parameter values across all packages.

        Iterates over all packages and updates specified parameters.

        Parameters
        ----------
        d : dict
            Dictionary with structure {key_name: value}
        """
        for pack_name_item, pack_val_item in self.parameters.items():
            for key_name_item, key_val_item in d.items():
                s = f"Looking for {key_name_item} in {pack_name_item}"
                print(s)

                if key_name_item not in pack_val_item:
                    continue

                else:
                    s = f"Changing {key_name_item} in package {pack_name_item} to {key_val_item}"
                    print(s)
                    # Activates the setter of the Parameter.value
                    self.parameters[pack_name_item][key_name_item] = Parameter(key_val_item)

    def script_sanitize_unwanted_parameters(self):
        unwanted = [
            "extension",
            "unitnumber",
            "filenames",
            "ftlfree",
            "ftlunit",
            "MFStyleArr",
            "DRYCell",
            "Legacy99Stor",
            "FTLPrint",
            "NoWetDryPrint",
            "OmitDryBud",
            "AltWTSorb",
            "dtype",
        ]

        for unwanted_item in unwanted:
            for key in self.parameters:
                if unwanted_item in self.parameters[key]:
                    del self.parameters[key][unwanted_item]

    def script_sanitize_return_all_data(self):
        mal_params = {"DRT": ["options"], "LAK": ["flux_data", "sill_data"]}
        for pck, params in mal_params.items():
            for param in params:
                if pck in self.parameters:
                    self.parameters[pck][param].return_all_data = True

        pass
