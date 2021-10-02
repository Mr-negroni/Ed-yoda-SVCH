number = (1,2,3,4,5,6,7,8,9)
odd =0
even = 0
for num in number:
    if(num%2==0):
        even = even +1
    else:
        odd = odd +1
print(" Even numbers are :")
print(even)
print('Odd numbers are :')
print(odd)