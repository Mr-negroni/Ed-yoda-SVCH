def sumL(list):
    sum = 0
    for i in range(0,len(X)):
        sum = sum+x[i]
    return sum

a = []
n = int(input("plese enter the lenght of list"))
for j in range(n):
    a.append(int(input("please enter the "+ str(j+1)+"th element")))
s =sum(a)
print("sum of the list is "+str(s))

