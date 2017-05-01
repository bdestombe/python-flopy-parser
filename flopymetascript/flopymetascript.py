# coding=utf-8
import argparse
import base64
import io
import os
import shutil
import sys
from contextlib import redirect_stdout

"""
This file handles the commandline interface

process can also be run, where all its arguments are file handles
"""


def main():
    """
    Provides the command line interface receives either filenames, stdin, or stdout, sanitizes them and calls the  
    process function with file handles.
    :return: 
    """
    usage = """
## With zipfiles
Try this first,
```bash
$ flopymetascript --outbytesfile output.zip --inbytesfile input.zip --logfile log.txt
```
input.zip is a zip-file that contains MODFLOW input files and a single .nam file. Its content is processed and 
written to output.zip. Some logging is written to log.txt. The `$`-sign should be omitted, and only refers to that the 
command is to be entered in the bash-commandline.

## Using pipes
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

You cannot send both outbase64file and logfile to stdout. They will be mixed and the resulting output file is not 
readable.
"""

    description = """
Converts a zip with MODFLOW input files to a zip containing Flopy script
"""

    epilog = """
No money is to be made with this service. I you find it useful, please donate to charity (be creative in choosing 
which one) and send me a note. Thanks! The author is not affiliated with the modflow family nor Flopy. This 
converter/generator uses the Flopy load function. Any errors/mistakes in the Flopy load functions propagate to the 
generated script. The author has absolutely no convidense in that this script is correct and is not responsible for 
the content and consequences of malicious scripts.
"""

    class MyParser(argparse.ArgumentParser):
        def error(self, message):
            sys.stderr.write('error: %s\n' % message)
            self.print_help()
            sys.exit(2)

    class input_action(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            if values.name == "<stdin>" or values.name == "<stdout>":
                raise argparse.ArgumentTypeError("Cannot use stdin for inbytesfile or stdout for outbytesfile")
            setattr(namespace, self.dest, values)

    parser = MyParser(prog='flopymetascript',
                      usage=usage,
                      description=description,
                      epilog=epilog)
    parser.add_argument('--version', action='version', version='%(prog)s 0.1.0')

    inputs = parser.add_mutually_exclusive_group()
    output = parser.add_mutually_exclusive_group()

    inputs.add_argument('--inbase64file', type=argparse.FileType('r'),
                        required=False, help='Filename or - for stdin of the input zipfile')
    output.add_argument('--outbase64file', type=argparse.FileType('w'),
                        required=False, help='Filename or - for stdout of the output zipfile')
    inputs.add_argument('--inbytesfile', type=argparse.FileType('rb'),
                        required=False, action=input_action, help='Filename of the input zipfile')
    output.add_argument('--outbytesfile', type=argparse.FileType('wb'),
                        required=False, action=input_action, help='Filename of the output zipfile')
    parser.add_argument('--logfile', type=argparse.FileType('w'),
                        required=False, help='Filename or - for stdout of the logfile')

    # Access the arguments as a dictionary
    kwargs = vars(parser.parse_args())

    # Pass all the arguments to the process function
    process(**kwargs)


def process(inbase64file=None, outbase64file=None,
            inbytesfile=None, outbytesfile=None,
            logfile=None):
    """
    All arguments are filehandles. Assumes sane filehandles, no checking for incompatible stdin stdout combinations.

    :param logfile: File handle with a write utf8 attribute of the logfile
    :param inbase64file: File handle with a read utf8 attribute of the input zipfile and encoded with base64
    :param outbase64file: File handle with a write utf8 attribute of the output zipfile and is encoded with base64
    :param inbytesfile: File handle with a read bytes attribute of the input zipfile
    :param outbytesfile: File handle with a write bytes attribute of the output zipfile
    :return: 
    """

    stdout_buf = io.StringIO()

    with redirect_stdout(stdout_buf):
        if logfile:
            print('\nRedirected the stdout to a temporary buffer\n')

        if logfile:
            print('\nAbout to import metafunctions.run\n')

        # Because flopy writes stuff to stdout while importing
        from .metafunctions import run

        if inbytesfile:
            print('\ninbytes file handle\n')
            inbytes = inbytesfile

        elif inbase64file:
            print('\ninbase64 file handle\n')

            inbytes = io.BytesIO()
            inbytes.write(base64.b64decode(inbase64file.read()))
            inbytes.seek(0)

        else:
            print('\nNo input files are given. I am about to throw an error\n')
            os.error('No input files are given')

        # To prevent error messages when run without arguments
        if inbytesfile or inbase64file:
            bytesZip = run(inbytes)
            bytesZip.seek(0)

        if logfile:
            stdout_buf.seek(0)
            shutil.copyfileobj(stdout_buf, logfile)

    # write output
    if outbytesfile:
        shutil.copyfileobj(bytesZip, outbytesfile)

    elif outbase64file:
        outbase64file.write(base64.b64encode(bytesZip.read()).decode())

    else:
        print('Im not doing anything')

    return
