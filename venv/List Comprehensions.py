
# Normal måde
f = open('test2.txt', 'r')
print(f.read())
f.close()

# Med comprehension
with open('test2.txt', 'r') as f:
    print(f.read())

# Normal
a = []
for x in range(4):
    a.append(x+1)
print(a)

# Comprehension
a = [x for x in [1, 2, 3, 4]]
print(a)

# Normal
l = []
for i in range(1, 10):
    l.append(i)
print(l)

# Comprehension
k = [i for i in range(1, 10)]
print(k)

# Flere eksempler

b = [x for x in range(1, 10) if x%2 == 0]
print(b)

b = [x  if x%2 == 0 else 'un-even'  for x in range(1, 10)]
print(b)

# Nested Loops

l = []
for i in range(3):
    for j in range(2):
        l.append((i, j))
print(l)

l = [(i,j) for i in range(3) for j in range(2)]
print(l)