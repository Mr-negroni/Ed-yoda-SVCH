class Powr():
    
    def perform (self):
        result = 1
        for i in range(self.powrr):
            result=result*self.number
        print("the result is")
        print(result)
        
i = Powr()

i.number = int(input("enter the number "))
i.powrr = int(input("enter the power of the number "))
i.perform()
