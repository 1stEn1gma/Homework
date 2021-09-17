a = str(input("Введите строку:"))
b = sorted(a)
for x in b:
    if b.count(x) != 1:
        while b.count(x) != 1:
            b.remove(x)
myDict = {}
for x in b:
    myDict[x] = a.count(x)
print(myDict) 