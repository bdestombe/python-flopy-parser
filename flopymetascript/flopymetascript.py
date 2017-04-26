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
    The base64 input and output can either be a filename or a pipe.

    # Example usage:

    $ python metascript.py --outbytesfile output.zip --inbytesfile input.zip
    input.zip is a zip-file that contains MODFLOW input files and a single .nam file. Its content is processed and 
    written to output.zip.

    $ openssl base64 -in input.zip -out input.zip.b64
    $ python metascript.py --outbytesfile output.zip --inbase64file input.zip.b64
    input.zip is encoded to base64 and is used as input file for metascript.py

    $ python metascript.py --outbytesfile output.zip --inbase64file - < input.zip.b64
    The content of input.zip.b64 is streamed/piped to metascript.py

    $ openssl base64 -in input.zip | python metascript.py --outbytesfile output.zip --inbase64file -
    The same as what is done previously, however input.zip is encoded and instead of writing it to a file, it is passed
    as stdin to the inbase64file argument.

    todo:
    - include setuptools
    - prepare tests. pymake check tools to compare two 
    """

    usage = """
    Example usage:

    $ python metascript.py --outbytesfile output.zip --inbytesfile input.zip
    input.zip is a zip-file that contains MODFLOW input files and a single .nam file. Its content is processed and 
    written to output.zip.

    $ openssl base64 -in input.zip -out input.zip.b64
    $ python metascript.py --outbytesfile output.zip --inbase64file input.zip.b64
    input.zip is encoded to base64 and is used as input file for metascript.py

    $ python metascript.py --outbytesfile output.zip --inbase64file - < input.zip.b64
    The content of input.zip.b64 is streamed/piped to metascript.py

    $ openssl base64 -in input.zip | python metascript.py --outbytesfile output.zip --inbase64file -
    The same as what is done previously, however input.zip is encoded and instead of writing it to a file, it is passed
    as stdin to the inbase64file argument.

    todo:
    - include setuptools
    - prepare tests. pymake check tools to compare two 
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

    parser = MyParser(prog='metascript',
                      usage=usage,
                      description=description,
                      epilog=epilog)
    parser.add_argument('--inbase64file', type=argparse.FileType('r'),
                        required=False)
    parser.add_argument('--outbase64file', type=argparse.FileType('w'),
                        required=False)
    parser.add_argument('--inbytesfile', type=argparse.FileType('rb'),
                        required=False)
    parser.add_argument('--outbytesfile', type=argparse.FileType('wb'),
                        required=False)
    parser.add_argument('--logfile', type=argparse.FileType('w'),
                        required=False)

    # Access the arguments as a dictionary
    kwargs = vars(parser.parse_args())

    # Pass all the arguments to the process function
    process(**kwargs)


def process(inbase64file=None, outbase64file=None,
            inbytesfile=None, outbytesfile=None,
            logfile=None):
    """
    bytefiles can not be used for piping. because printing to stdin and stdout assumes utf8.

    :param logfile: 
    :param inbase64file: File handle that has a read utf8 attribute that are encoded with base64
    :param outbase64file: File handle that has a write utf8 attribute that are encoded with base64
    :param inbytesfile: File handle that has a read bytes attribute
    :param outbytesfile: File handle that has a write bytes attribute
    :return: 
    """
    stdout_buf = io.StringIO()

    with redirect_stdout(stdout_buf):
        # Because flopy writes stuff to stdout while importing
        from .metafunctions import run

        if inbytesfile:
            inbytes = inbytesfile

        elif inbase64file:
            inbytes = io.BytesIO()
            inbytes.write(base64.b64decode(inbase64file.read()))
            inbytes.seek(0)

        else:
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
