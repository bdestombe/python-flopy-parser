# flopymetascript
Converts a zip with MODFLOW input files to a zip containing Flopy script

No money is to be made with this service. I you find it useful, please donate to charity (be creative in choosing 
which one) and send me a note. Thanks! The author is not affiliated with the modflow family nor with Flopy. This 
converter/generator uses the Flopy load function. Any errors/mistakes in the Flopy load functions propagate to the 
generated script. The author has absolutely no convidense in that this script is correct and is not responsible for 
the content and consequences of malicious scripts.

# Use cases
- You are coming from a different modeling environment and want to start using Flopy
- You want to clean up your flopy script/notebook. Having different scripts loading from different sources might prove difficult to understand.
- You want to add a description (and default value) to your parameters
- You want to check someone else's MODFLOW input files / Flopy script

# Install
```bash
pip install https://github.com/bdestombe/flopymetascript/zipball/master
```
The flopymetascript package added to system's `$PATH` and is reachable from any directory. Check if everything works by typing in any directory,
```bash
flopymetascript --help
```
Uninstall with,
```bash
pip uninstall flopymetascript
```

# Example usage from the commandline:
## With zipfiles
```bash
$ flopymetascript --outbytesfile output.zip --inbytesfile input.zip --logfile log.txt
```
input.zip is a zip-file that contains MODFLOW input files and a single .nam file. Its content is processed and 
written to output.zip. Some logging is written to log.txt. The `$`-sign should be omitted, and only refers to that the command is to be entered in the bash-commandline.

## Using pipes
```bash
$ openssl base64 -in input.zip -out input.zip.b64
$ flopymetascript --outbytesfile output.zip --inbase64file input.zip.b64
```
input.zip is encoded to base64 and is used as input file for metascript.py

```bash
$ flopymetascript --outbytesfile output.zip --inbase64file - < input.zip.b64
```
The content of input.zip.b64 is streamed/piped to metascript.py

```bash
$ openssl base64 -in input.zip | flopymetascript --outbytesfile output.zip --inbase64file -
```
The same as what is done previously, however input.zip is encoded and instead of writing it to a file, it is passed
as stdin to the inbase64file argument.

```bash
$ openssl base64 -in input.zip | flopymetascript --outbase64file utput.zip --inbase64file - --logfile -
```
The log file is printed to stdout.

You cannot send both outbase64file and logfile to stdout. They will be mixed and the resulting output file is not readable.

# Example usage in python
This might need somework and is subject to change in the future.

```python
from flopymetascript.flopymetascript import process

# fn = 'input.zip.b64'
# inbase64file = open(fn, 'r')
# fn = 'output.zip.b64'
# outbase64file = open(fn, 'w')
fn = 'input.zip'
inbytesfile = open(fn, 'rb')   # Dont forget the b
fn = 'output.zip'
outbytesfile = open(fn, 'rb')  # Dont forget the b
fn = 'log.txt'
logfile = open(fn, 'w')

process(inbytesfile=inbytesfile, outbytesfile=outbytesfile, logfile=logfile)

inbytesfile.close()
outbytesfile.close()
logfile.close()
```


# todo:
- prepare tests. Use the pymake check tools to compare the origional outcomes with the ones generated by the newly created Flopy script
