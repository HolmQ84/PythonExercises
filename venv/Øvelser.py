a = 'Hej med dig, hvordan går det med dig?'

def removeVowels(x):
    a = []
    count = 0
    vowels = ['a','e','i','u','o','y','æ','ø','å']
    for y in range(len(x)):
        if x[y] in vowels:
            x.replace(x[y], "")

        if (x[y] == ' '):
            a.append(x[count:y])
            count = y
    a.append(x[count:])
    return a

print(removeVowels(a))

