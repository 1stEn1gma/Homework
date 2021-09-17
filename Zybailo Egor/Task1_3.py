l = ['red', 'white', 'black', 'red', 'green', 'black']
for x in l:
    if l.count(x) != 1:
        l.remove(x)
print(sorted(l)) 