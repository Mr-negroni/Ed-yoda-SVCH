class Cinema:
    def __init__(self,Rows,Columns):
        self.L = dict()
        self.price = 0
        self.Final_Sale = 0
        self.theatre = list()
        self.theatre = [['S' for _ in range(Columns+1)] for _ in range(Rows+1)]
        for i in range(Columns+1):
            self.theatre[0][i]=i
        for i in range(Rows+1):
            self.theatre[i][0]=i
            self.theatre[0][0]= ' '

    def Display(self):
        print("1. Show the Seats")
        print("2. Buy a Ticket ")
        print("3. Statistics")
        print("4. Show booked Ticket User Info")
        print("0. Exit")
        return int(input())
    def Show_the_Seats(self):
        print("Cinema : \n")
        for l in self.theatre:
            for m in l :
                print(m,end = ' ')
            print('\n')
    def Buy_a_Ticket(self,Rows,Columns):
        R1 = int(input("Enter the Row : "))
        C1 = int(input("Enter the Column :"))
        self.price = self.costing(R1,Rows,Columns)
        print("The Price of the Chosen Seat is :  ",format(self.price))
        x = input("Do you Want to book a ticket, Yes or No : ")
        if(x=='YES' or x=='Yes' or x=='yes'):
            self.Final_Sale = self.Final_Sale + self.price
            self.name = input("Please enter the name : ")
            self.gender = input("Please enter the gender : ")
            self.age = int(input("Please enter your age : " ))
            self.Phone_no = int(input("Please enter your Phone Number : "))
            self.L[(R1,C1)] = [self.name,self.gender,self.age,self.price,self.Phone_no]
            self.theatre[R1][C1] = 'B'
            self.Show_the_Seats()
            print("     BOOKED SUCCESSFULLY !     \n")
        else:
            pass
    def costing(self,R1,Rows,Columns):
        if(Rows*Columns <=60):
            return 10
        elif(Rows*Columns > 60):
            if(R1<Rows/2):
                return 10
            else:
                return 8
    def Statistics(self,Rows,Columns):
        self.Show_the_Seats()
        z = len(self.L)
        print("1. Number of Purchased Tickets  : ",format(z))
        perc = ((z/(Rows*Columns)))*100
        form_perc = '{:.2f}'.format(perc)
        print("2. Percentage of Tickets Booked : ",format(form_perc))
        print("3. Current Income is            :",format(self.Final_Sale))
        if(Rows*Columns<60):
            net_income = Rows*Columns*10
        else:
            if(Rows%2==0):
                net_income = (Rows/2*Columns*10)+(Rows/2*Columns*8)
            else:
                net_income = (abs(Rows/2)*Columns*10)+(abs(Rows/2)*Columns*8)
        print("4. Total Income is              : ",format(net_income))
        print('\n')
    def Show_Booked_ticket_info(self):
        R2 = int(input("Enter the Row : "))
        C2 = int(input("Enter the Columns : "))
        if(R2,C2) in self.L :
            info = self.L.get((R2,C2))
            print("\nName         : ",info[0])
            print('Gender       : ',info[1])
            print('Age          : ',info[2])
            print('Ticket Price : ',info[3])
            print('Phone No     : ',info[4])
            print('\n')
        else:
            print("Ticekts are not booked for the following Seats")
        
Rows12 = int(input("Enter the Row : "))
Columns12 = int(input("Enter the number of Seats in a Row : "))
k = 6
cinema_1 = Cinema(Rows12,Columns12)
while k!=0:
    k = cinema_1.Display()
    if(k==1):
        cinema_1.Show_the_Seats()
    elif(k==2):
        cinema_1.Buy_a_Ticket(Rows12,Columns12)
    elif(k==3):
        cinema_1.Statistics(Rows12,Columns12)
    elif(k==4):
        cinema_1.Show_Booked_ticket_info()
    


