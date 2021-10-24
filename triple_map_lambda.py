a = int(input("enter lenght of list"))
b = []
for i in range(a):
    b.append(int(input()))
print(b)
result = map(lambda y : y*3,b)
print(list(result))