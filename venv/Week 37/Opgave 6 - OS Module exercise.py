# Opgave 6.
# os_exercise.py
# Do the following task using the os module
# 1. create a folder and name the folder 'os_exercises.'
# 2. In that folder create a file. Name the file 'exercise.py'
# 3. get input from the console and write it to the file.
# 4. repeat step 2 and 3 (name the file something else).
# 5. read the content of the files and and print it to the console.

import os

# 1. Create a folder 'os_exercises'
directory = 'C:/Users/marti/PycharmProjects/PythonExercises/venv/Week 37/'
name = 'os_exercises'
path = directory+name

if not os.path.exists(name):
    os.mkdir(path)

# 2. Create a file in that folder called 'exercise.py'

os.chdir(path)
open('exercise1.py', 'w')

# 3.

text = input('Write something:\n=> ')
with open('exercise1.py', 'w') as f:
    f.write(text)

# 4.

text = input('Write something:\n=> ')
with open('exercise2.py', 'w') as f:
    f.write(text)

# 5.

with open('exercise1.py', 'r') as f:
    with open('exercise2.py', 'r') as g:
        print(f.read()+g.read())