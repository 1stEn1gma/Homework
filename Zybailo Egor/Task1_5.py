myListOfDict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
                {"VIII": "S007"}]
m = []
for x in myListOfDict:
    for b in x:
        m.append(x.get(b))
print(m)
for x in m:
    if m.count(x) != 1:
        m.remove(x)
print(m) 