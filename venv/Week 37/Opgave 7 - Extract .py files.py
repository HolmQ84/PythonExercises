# Opgave 7.
# Create a commandline utillity (program) that when run takes 1-3 commandline arguments where:
#
#   * the first is the name of a directory in play
#   * the second (optional) is a –flag (–todir <dirname>) that specifies where the files in that directory should be copied to.
#   * the third (optional) is a –flag (–zip <filename>) that specifies if the files should be zipped and what the zip file should be called.
#
# So if you run the program like this python extract.py . --todir /tmp/ --zip archive.zip you should copy all files in the current directory (.) to a new tmp directory and the .py files should be put in a zip folder names archive.zip.
#
# Task A:
# Copy all .py files in a given directory to a new folder.
#
# Task B:
# Zip all .py files in a given directory and put the zip file in the specified folder.

import sys
import os
import subprocess
from zipfile import ZipFile


def main(argv):
    input_check(argv)

    # A
    # list all files in folder
    x = os.listdir(argv[1])

    # list all .py files
    pyfiles = [i for i in x if i[-3:] == '.py']

    # create new dir
    os.mkdir(argv[3])

    # copy all files in list --todir
    for i in pyfiles:
        subprocess.run(['cp', i, argv[3]])

    # B
    with ZipFile(argv[3] + '/archive.zip', 'w') as zf:
        for file in pyfiles:
            zf.write(file)


def input_check(argv):
    if len(argv) < 2:
        print('Usage: python extract.py [.] [--todir <<tmp/>>] {--zip <<filename.zip>>}')
        sys.exit()
    if len(argv) == 3 and argv[2] != '--todir':
        print('Usage: python extract.py [.] [--todir <<tmp/>>] {--zip <<filename.zip>>}')
        sys.exit()


main(sys.argv)