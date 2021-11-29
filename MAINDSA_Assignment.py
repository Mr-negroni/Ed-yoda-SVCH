def pair():
    def findpair(nums,target):
        nums.sort()
        low = 0
        hi = len(nums)-1
        while low<hi:
            if(nums[low]+nums[hi]==target):
                print("Pair Found ({},{})".format(nums[low],nums[hi]))
                low = low+1
                hi = hi -1
            elif (nums[low]+nums[hi]<target):
                low = low+1
            elif (nums[low]+nums[hi]>target):
                hi = hi-1
    
    lens = int(input("Enter the lenght of list "))
    numbers = list() 
    for i in range(0,lens):
        numbers.append(int(input("Enter the {}th Number ".format(i+1))))
    b = int(input("Enter the Sum of which you want pairs of "))
    findpair(numbers,b)
def Rot():
    a = input("Enter the First String ")
    b = input("Enter the second string to check whether is it a rotation of previous or not ")
    c = a+b
    if a in c and b in c :
        print("String is a rotation of other string")
    else:
        print("String is not a rotation of previous string")
def Rev():
    def reverse(nums):
        low = 0
        hi = len(nums)-1
        while low<hi:
            nums[low],nums[hi]=nums[hi],nums[low]
            low+=1
            hi-=1
        print(nums)
    lens = int(input("Enter the lenght of list "))
    numbers = list()
    for i in range(0,lens):
        numbers.append(int(input("Enter the {}th Number ".format(i+1))))
    reverse(numbers)
def NRC():
    def firstnonrepeatingchar(str):
        hash_map = {}
        char_order = []
        for x in str:
            if x in hash_map:
                hash_map[x]+=1
            else:
                hash_map[x]=1
                char_order.append(x)
        for y in char_order:
            if hash_map[y]==1:
                return y
            else:       
                pass
        print("Either all the characters are repeated or the String is NULL!!")
    string = input('Enter the String to find first non repeating character ')
    print(firstnonrepeatingchar(string))

def Hanoi():
    def Tower_of_hanoi(n,fro,to,aux):
        if n==1:
            print("Move disk {} from {} to {}".format(n,fro,to))
        else:
            Tower_of_hanoi(n-1,fro,aux,to)
            print("move disk {} from  {} to {}".format(n,fro,to))
            Tower_of_hanoi(n-1,aux,to,fro)
    a = int(input("Enter the number of disk "))
    R1= input("Name of Rod 1 ")
    R2= input("Enter the name of rod 2 ")
    R3= input("Enter the name of rod 3 ")
    Tower_of_hanoi(a,R1,R2,R3)
def PTP():
    def operator(x):
        if (x =='+' or x=='-' or x=='/' or x=='*'):
            return True
    def Post_Pre(post_exp):
        s = []
        l = len(post_exp)
        for i in range(l):
            if(operator(post_exp[i])):
                op1 = s[-1]
                s.pop()
                op2 = s[-1]
                s.pop()
                temp = post_exp[i]+op2+op1
                s.append(temp)
            else:
                s.append(post_exp[i])
        for i in s:
            print(i)
    y = input("Enter the Post Fix Expression")
    Post_Pre(y)

def PreTI():
    def operator(x):
        if (x =='+' or x=='-' or x=='/' or x=='*'):
            return True
    def Prefix_infix(pre_exp):
        s = []
        i = len(pre_exp)-1
        while i>=0:
            if not operator(pre_exp[i]):
                s.append(pre_exp[i])
                i-=1
            else:
                str = '('+ s.pop()+pre_exp[i]+s.pop()+')'
                s.append(str)
                i-=1
        return s.pop()
    y = input("Enter the Prefix to change to Infix ")
    print(Prefix_infix(y))
def Balans():
    def balanced_Brackets(exp):
        s = []
        for i in exp:
            if i=='('or i=='[' or i=='{':
                s.append(i)
            else:
                if not s:
                    return False
                curr_char = s.pop()
                if curr_char == '(':
                    if i!= ')':
                        return False
                if curr_char == '{':
                    if i != '}':
                        return False
                if curr_char == '[':
                    if i != ']':
                        return False
        if s:
            return False
        return True
    y = input("Enter the Bracket Snippet")
    print(balanced_Brackets(y))
def RevStack():
    class Stack:
        def __init__(self):
            self.element = []
        def push(self,value):
            self.element.append(value)
        def pop(self):
            return self.element.pop()
        def empty(self):
            return self.element == []
        def show(self):
            for val in reversed(self.element):
                print(val)
    #insert element at last
    def bottominsert(s,valu):
        if s.empty():
            s.push(valu)
        else:
            popped = s.pop()
            bottominsert(s,valu)
            s.push(popped)
    def Reverse(s):
        if s.empty():
            pass
        else:
            popped = s.pop()
            Reverse(s)
            bottominsert(s,popped)
    a = Stack()
    k = 1
    while k!=0:
        x = int(input('What do you want to do : 1. Push 2. Pop 3. Show 4. Reverse 0. Exit '))
        if x==1:
            b = int(input("Enter the value to push "))
            a.push(b)
        elif x ==2 :
            print("The popped element is {} ".format(a.pop()))
        elif x ==3 :
            a.show()
        elif x ==4:
            Reverse(a)
            a.show()
        else:
            k = 0
def FindSmall():
    from collections import deque
    class MinStack:
        def __init__(self):
            self.s = deque()
            self.min = None
        def push(self, x):
            if not self.s:
                self.s.append(x)
                self.min = x
            elif x > self.min:
                self.s.append(x)
            else:
                self.s.append(2*x - self.min)
                self.min = x
        def pop(self):
            if not self.s:
                self.print("Stack underflow!!")
            top = self.s[-1]
            if top < self.min:
                self.min = 2*self.min - top
            self.s.pop()
        def minimum(self):
            return self.min
    s = MinStack() 
    s.push(6)
    print(s.minimum())
    s.push(7)
    print(s.minimum())
    s.push(5)
    print(s.minimum())
    s.push(3)
    print(s.minimum())
    s.pop()
    print(s.minimum()) 
    s.pop()
    print(s.minimum())
k = 1
while k!= 0:
    print("1. Find all pair of integer whose sum is equal to a given number")
    print("2. Reverse an Array In Place")
    print("3. Check whether Two strings are rotation of each other")
    print("4. Find the first Non repeated Character From a String")
    print("5. Tower of Hanoi")
    print("6. Postfix to Prefix Conversion")
    print("7. Prefix to Infix Conversion")
    print("8. Balancing of Brackets in a Snippet")
    print("9. Reverse a Stack")
    print("10. Find Smallest number using Stack")
    print('Press enter to Exit ')
    g = int(input("Choose one from the Above "))
    if g ==1:
        pair()
    elif g ==2:
        Rev()
    elif g ==3:
        Rot()
    elif g ==4:
        NRC()
    elif g ==5:
        Hanoi()
    elif g ==6:
        PTP()
    elif g ==7:
        PreTI()
    elif g ==8:
        Balans()
    elif g ==9:
        RevStack()
    elif g ==10:  
        FindSmall()
    else:
        k = 0      