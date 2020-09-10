# Læs fra filer.

# God måde
f = open('test.txt')
print(f.read())
print('********************\n')
f = open('test.txt')
print(f.readline())
print('********************\n')
f = open('test.txt')
print(f.readlines())
f.close()

# Bedre måde
with open('test.txt', 'r') as f:
    print(f.read())

#Skriv til filer

s = open('test.txt', 'a')
s.write('Hello from Denmark\n')