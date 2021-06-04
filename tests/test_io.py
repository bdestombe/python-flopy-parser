import os
from flopyparser.flopyparser import process


"""
0. process zip in to zip out
    if no serious errors occured, happy
1. unzip the input files to temporary directory
2. unzip output files to temperary directory
3. evaluate python script, model_ws -> temporary directory and write the the input files


"""

inbytesfn = os.path.abspath(os.path.join('tests', 'data', 'BW.zip'))    # Dont forget the b flag when opening the file
outbytesfn = 'output.zip'   # Dont forget the b flag when opening the file
logfn = 'log.txt'


def test_write_to_zip():
    with open(inbytesfn, 'rb') as inbytesfh, \
            open(outbytesfn, 'wb') as outbytesfh, \
            open(logfn, 'w') as logfh:
        process(inbytesfile=inbytesfh,
                outbytesfile=outbytesfh,
                logfile=logfh)

    os.remove(outbytesfn)
    os.remove(logfn)
    pass
