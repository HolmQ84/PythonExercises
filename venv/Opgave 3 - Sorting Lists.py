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
