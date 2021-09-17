N = int(input('Введите число: '))
myList = []
for d in range(1, N + 1):
    if N % d == 0:
        myList.append(d)
print(myList) 