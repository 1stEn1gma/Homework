a = 10
b = 17
c = 10
d = 14
print(" ", end=' ')
for j in range(d - c + 1):
    print(j + c, end=' '),
print("")
while a != b+1:
    print(a, end=" ")
    k = c
    while k != d+1:
        print(a*k, end=" ")
        k += 1
    print("")
    a += 1 