# Opgave 2.

b = input("Enter a string: ")

def removeVowels(string):
    for i in ['a', 'e', 'i', 'o', 'u', 'y', ' ']:
        string = string.lower().replace(i, '')

    return sorted(string)

print(removeVowels(b))

# Opgave 3.

# 1. Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])
names = ['Martin', 'Patrick', 'Nicholas', 'Victor']
# 2. Sort this list by using the sorted() build in function.
sortedNames = sorted(names)
print(sortedNames)
# 3. Sort the list in reversed order.
sortedNamesReversed = sorted(names, reverse=True)
print(sortedNamesReversed)
# 4. Sort the list on the length of the name.
sortedNamesByLength = sorted(names, key=len)
print(sortedNamesByLength)
# 5. Sort the list based on the last letter in the name.
def last(list):
    return list[-1]
sortedByLastLetter = sorted(names, key=last)
print(sortedByLastLetter)
# 6. Sort the list with the names where the letter ‘a’ is in the name first.
def a_in(list):
    if 'a' in list.lower():
        return False
    return True
sortedByALetter = sorted(names, key=a_in)
print(sortedByALetter)

# Opgave 4.

# 1. Create a file and call it lyrics.txt (it does not need to have any content)

open('lyrics.txt', 'w')

# Create a new file and call it songs.docx and in this file write 3 lines of text to it.

songs = open('songs.txt', 'a')
songs.writelines('Godmorgen\n')
songs.write('God eftermiddag\n')
songs.write('Godaften\n')

#open and read the content and write it to your terminal window.
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