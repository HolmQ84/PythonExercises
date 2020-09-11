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

