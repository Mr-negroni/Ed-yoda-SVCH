def count(string):
    upper =0
    lower = 0
    for i in range(0,len(string)):
        if ord(string[i])>=97 and ord(string[i])<=122:
            lower = lower+1
        elif ord(string[i])>=65 and ord(string[i])<=90:
            upper = upper+1
    print(" Number of Lower Letter are {} ",format(lower))
    print("NUmber of upper letter are {}",format(upper))

a = input(" please a enter a string to count number of lower and upper letters")
count(a)