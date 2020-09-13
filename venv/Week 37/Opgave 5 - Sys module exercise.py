# Opgave 5.
# Create a commandline tool that checks if the required aguments are present when you run the program,
# and if not tells you what is missing to run the program.
# If you run python python script.py the program should print an error saying Usage:
# python script.py [-it]{--rm} where the [] means required and the {} means optional.

import sys

def message(x):
    if len(x) > 0:
        print(x[1])

    if len(x) > 1:
        print(x[1])
        print(x[2])

message(sys.argv)