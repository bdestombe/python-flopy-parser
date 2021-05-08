[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.573584.svg)](https://doi.org/10.5281/zenodo.573584)
[![Build Status](https://travis-ci.com/bdestombe/flopymetascript.svg?branch=master)](https://travis-ci.com/bdestombe/flopymetascript)

# Table of Content
- [Use Cases](#use-cases)
- [Highlights](#highlights)
- [Install](#install)
- [Example usage from the commandline](#example-usage-from-the-commandline)
  - [Using zipfiles from the commandline](#using-zipfiles-from-the-commandline)
  - [Using pipes from the commandline](#using-pipes-from-the-commandline)
- [Example usage in Python](#example-usage-in-python)
  - [Using zipfiles in Python](#using-zipfiles-in-python)
  - [Using as a function in Python](#using-as-a-function-in-python)


# flopymetascript
Converts a zip with MODFLOW input files to a zip containing Flopy script in different formats. This Flopy (Python) script can generate the intitial MODFLOW input files.

<img src="https://raw.githubusercontent.com/bdestombe/flopymetascript/master/assets/figures/workflow.png" alt="workflow" style="width:50;height:20">

It should work for all packages of MODFLOW, MT3D, and SEAWAT. For a complete list, see the 
[Packages with default values](./wiki_default_parameters.md) and the load supported packages [on the Flopy website](https://github.com/modflowpy/flopy/blob/develop/docs/supported_packages.md).

The flopymetascript is continously tested with several benchmark modflow models. This ensures that the generated python scripts contain valid code and produce the same heads and flow as the benchmark input files.

The software is available under MIT license. The author has absolutely no convidense in that the software is correct and is not responsible for the content and consequences of malicious scripts. I you find it useful, please consider donating to charity (be creative in choosing which one) and send me a note (or create and close an issue). Thanks! The author is not affiliated with the modflow family nor with Flopy. This converter/generator uses the Flopy load function. Any errors/mistakes in the Flopy load functions propagate silently in to the generated script.

# Use cases
- You are coming from a different modeling environment and want to start using Flopy
- Clean up your flopy script/notebook
- Add a description (and default value) to your parameters
- Check someone else's MODFLOW input files / Flopy script
- Check homework assignments
- Start from scratch by adding your own packages


# Highlights
- Returns .ipynb, py, tex, html, markdown, and rst file of your MODFLOW input files
- Consistent and clean markup is used
- All the parameters are defined explicitely
- A description is loaded and interpreted from the flopy package directly. The same description as in the docs (modflowpy.github.io/flopydoc/) is used.
- Makes use of smart broadcasting to reduce the size of the arrays printed to the script.


# Install
Enter in the terminal,
```bash
$ pip install https://github.com/bdestombe/flopymetascript/archive/master.zip
```
The `$`-sign should be omitted, and only refers to that the command is to be entered in the bash-commandline. The flopymetascript package added to system's `$PATH` and is reachable from any directory. Check if everything works by typing in any directory,
```bash
$ flopymetascript --help
```
Uninstall with,
```bash
$ pip uninstall flopymetascript
```

# Example usage from the commandline:
## Using zipfiles from the commandline
Try this first,
```bash
$ flopymetascript --outbytesfile output.zip --inbytesfile input.zip --logfile log.txt
```
input.zip is a zip-file that contains MODFLOW input files and a single .nam file. Its content is processed and 
written to output.zip. Some logging is written to log.txt. 

## Using pipes from the commandline
Might be of interest when using flopymetascript as webservice.
```bash
$ openssl base64 -in input.zip -out input.zip.b64
$ flopymetascript --outbytesfile output.zip --inbase64file input.zip.b64
```
Here, in the first line `input.zip` is encoded to base64 and is used in the second line as input file for flopymetascript.

```bash
$ flopymetascript --outbytesfile output.zip --inbase64file - < input.zip.b64
```
The content of input.zip.b64 is streamed/piped to flopymetascript

```bash
$ openssl base64 -in input.zip | flopymetascript --outbytesfile output.zip --inbase64file -
```
The same as what is done previously, however input.zip is encoded and instead of writing it to a file, it is passed
as stdin to the inbase64file argument of flopymetascript.

```bash
$ openssl base64 -in input.zip | flopymetascript --outbase64file utput.zip --inbase64file - --logfile -
```
The log file is printed to stdout.

You cannot send both outbase64file and logfile to stdout. They will be mixed and the resulting output file is not readable.

# Example usage in Python 
## Using zipfiles in Python
```python
from flopymetascript.flopymetascript import process

inbytesfn = 'input.zip'      # Dont forget the b flag when opening the file
outbytesfn = 'output.zip'.   # Dont forget the b flag when opening the file
logfn = 'log.txt'

with open(inbytesfn, 'rb') as inbytesfh, \
        open(outbytesfn, 'wb') as outbytesfh, \
        open(logfn, 'w') as logfh:
    process(inbytesfile=inbytesfile, 
            outbytesfile=outbytesfile, 
            logfile=logfile)
```

## Using as a function in Python
This example loads a name-file and overwrites the `dis` and `bas6` package with the default parameter values. If `dis` and `bas6` were not loaded with the name file, they are added. Extra options are now accessible, such as `print_descr` for printing the parameter description (bool), `width` for the desired line width of the produced script (int, number of characters), `use_yapf` to use Google's package to format the produced code (bool, conversion becomes slow).  
```python
from flopymetascript.model import Model

mp = Model(load_nam='path_to_namfile.nam', add_pack=['dis', 'bas6'])
fn = 'path_to_jupyter_notebook.ipynb'

mp.write_script_model2string(fn=fn,
                             print_descr=True,
                             width=99,
                             use_yapf=True)
```
