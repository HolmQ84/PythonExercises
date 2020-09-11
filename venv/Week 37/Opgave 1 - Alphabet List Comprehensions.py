# 1. Create a list of capital letters in the english alphabet

l1 = [chr(i) for i in range (65, 91)]
print(l1)

# 2. Create a list of capital letter from the english aplhabet, but exclude 4 with the Unicode code point of either 70, 75, 80, 85.

l2 = [chr(i) for i in range (65, 91) if not i in [70, 75, 80, 85]]
print(l2)

# 3. Create a list of capital letter from from the english aplhabet, but exclude every second between F & O.

l3 = [chr(i) for i in range (65, 91) if not i in range (70, 80, 2)]
print(l3)
