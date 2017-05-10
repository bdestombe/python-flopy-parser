[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.573584.svg)](https://doi.org/10.5281/zenodo.573584)
# flopymetascript
Converts a zip with MODFLOW input files to a zip containing Flopy script in different formats. This Flopy (Python) script can generate the intitial MODFLOW input files.

<img src="https://raw.githubusercontent.com/bdestombe/flopymetascript/master/assets/figures/workflow.png" alt="workflow" style="width:50;height:20">

It should work for all packages of MODFLOW, MT3D, and SEAWAT. For a complete list, see the 
[Packages with default values](./wiki_default_parameters.md) and the load supported packages [on the Flopy website](https://github.com/modflowpy/flopy/blob/develop/docs/supported_packages.md).

No money is to be made by the author with this package. The author has absolutely no convidense in that this script is correct and is not responsible for the content and consequences of malicious scripts. I you find it useful, please consider donating to charity (be creative in choosing which one) and send me a note (or create and close an issue). Thanks! The author is not affiliated with the modflow family nor with Flopy. This converter/generator uses the Flopy load function. Any errors/mistakes in the Flopy load functions propagate to the 
generated script.

# Use cases
- You are coming from a different modeling environment and want to start using Flopy
- Clean up your flopy script/notebook
- Add a description (and default value) to your parameters
- Check someone else's MODFLOW input files / Flopy script
- Check homework assignments
- Start from scratch by adding your own packages


# Advantages
- Returns .ipynb, py, tex, html, markdown, and rst file of your MODFLOW input files
- Consistent and clean markup is used
- All the parameters are defined explicitely
- A description is loaded and interpreted from the flopy package directly. The same description as in the docs (modflowpy.github.io/flopydoc/) is used.
- Makes use of smart broadcasting to reduce the size of the arrays printed to the script.


# Install
Enter in the terminal,
```bash
$ pip install flopymetascript
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
## With zipfiles
Try this first,
```bash
$ flopymetascript --outbytesfile output.zip --inbytesfile input.zip --logfile log.txt
```
input.zip is a zip-file that contains MODFLOW input files and a single .nam file. Its content is processed and 
written to output.zip. Some logging is written to log.txt. 

## Using pipes
Might be of interest when using flopymetascript as webservice of in docker containers.
```bash
$ openssl base64 -in input.zip -out input.zip.b64
$ flopymetascript --outbytesfile output.zip --inbase64file input.zip.b64
```
input.zip is encoded to base64 and is used as input file for flopymetascript

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

# Example usage in python
```python
from flopymetascript.flopymetascript import process

# fn = 'input.zip.b64'
# inbase64file = open(fn, 'r')
# fn = 'output.zip.b64'
# outbase64file = open(fn, 'w')
fn = 'input.zip'
inbytesfile = open(fn, 'rb')   # Dont forget the b
fn = 'output.zip'
outbytesfile = open(fn, 'wb')  # Dont forget the b
fn = 'log.txt'
logfile = open(fn, 'w')

process(inbytesfile=inbytesfile, outbytesfile=outbytesfile, logfile=logfile)

inbytesfile.close()
outbytesfile.close()
logfile.close()
```
or as a module,
```python
from flopymetascript.model import Model
import nbformat

mp = Model(load_nam='path_to_namfile.nam', add_pack=['dis', 'bas6'])
nb = mp.script_model2nb(use_yapf=False, print_descr=True)
fn = 'jupyter_notebook.ipynb'

with open(fn, 'w') as f:
    f.write(nbformat.writes(nb))
```

# Todo:
- Add a toggle to turn of the parameter description
- Add line width as parameter
