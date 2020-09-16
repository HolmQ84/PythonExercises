# Opgave 5.
# Create a commandline tool that checks if the required aguments are present when you run the program,
# and if not tells you what is missing to run the program.
# If you run python python script.py the program should print an error saying Usage:
# python script.py [-it]{--rm} where the [] means required and the {} means optional.

import sys

def check_syntax(x):
    if '-it' in x and '-rm' in x:
        print('Cool story bro!')
    elif "-it" not in x:
        print('not okay!')
    elif '-it' in x:
        print("Thats cool!")

message(sys.argv)