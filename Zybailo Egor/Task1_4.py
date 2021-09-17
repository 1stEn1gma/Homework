myDict = {'1': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
sorted_tuple = sorted(myDict.items(), key=lambda x: x[0])
for x in sorted_tuple:
    myDict[x[0]] = x[1]
print(myDict) 