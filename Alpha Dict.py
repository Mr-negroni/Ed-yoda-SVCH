b = []
for i in range(97,123):
    b.append(i)
c = []
for i in range(97,123):
    c.append(chr(i))
d ={}
for x in c:
    for y in b:
        d[x] =y
        b.remove(y)
        break
print(d)