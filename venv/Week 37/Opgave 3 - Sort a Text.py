# Opgave 3.

# Based on this exercise from last time sort it by using a list comprehensions instead.

string = 'Hello world'

# def sort_cons(s):
#     return [i for i in string if not ['a', 'e', 'i', 'o', 'u', 'y', ' ']]
#     for i in ['a', 'e', 'i', 'o', 'u', 'y', ' ']:
#         s = s.lower().replace(i, '')
#
#     return sorted(s)

def sort_cons(s):
    return sorted([i for i in s.lower() if not i in ['a', 'e', 'i', 'o', 'u', 'y', ' ']])

print(sort_cons(string))