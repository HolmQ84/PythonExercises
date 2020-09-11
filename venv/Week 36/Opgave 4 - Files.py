# Opgave 4.

# 1. Create a file and call it lyrics.txt (it does not need to have any content)

open('lyrics.txt', 'w')

# Create a new file and call it songs.docx and in this file write 3 lines of text to it.

songs = open('songs.txt', 'a')
songs.writelines('Godmorgen\n')
songs.write('God eftermiddag\n')
songs.write('Godaften\n')

# open and read the content and write it to your terminal window.
# you should use both the read(), readline(), and readlines() methods for this. (so 3 times the same output).

# 2. Read()
reader1 = open('songs.txt', 'r')
print(reader1.read())

# 3. Readline()
reader2 = open('songs.txt', 'r')
line = reader2.readline()
while line:
    print(line)
    line = reader2.readline()

# 4. Readlines()
reader3 = open('songs.txt', 'r')
for x in reader3.readlines():
    print(x)