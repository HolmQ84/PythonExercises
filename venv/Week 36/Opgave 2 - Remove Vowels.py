# Opgave 2.

b = input("Enter a string: ")

def removeVowels(string):
    for i in ['a', 'e', 'i', 'o', 'u', 'y', ' ']:
        string = string.lower().replace(i, '')

    return sorted(string)

print(removeVowels(b))
