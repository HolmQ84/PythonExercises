# Læs fra filer.

f = open('test.txt')
print(f.read())
print('********************')
f = open('test.txt')
print(f.readline())
print('********************')
f = open('test.txt')
print(f.readlines())

#Skriv til filer

s = open('test.txt', 'a')
s.write('Hello from Denmark\n')