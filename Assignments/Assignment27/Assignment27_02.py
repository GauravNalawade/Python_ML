class BankAccount:
    ROI=10.5

    def __init__(self,name,amount):
        self.Name=name
        self.Amount=amount

    def Deposit(self,Credited_Amt):
        if (Credited_Amt<=0):
            print("Credit Amount should be Greater than zero (0)")
        else:
            self.Amount += Credited_Amt

    def withdraw(self,Debited_Amt):
        if Debited_Amt<=0:
            print("Debit Amount should be Greater than zero")
        elif(Debited_Amt>self.Amount):
            print("Unable to withdraw Amount Insufficient balance:",self.Amount)
        else:
            self.Amount-=Debited_Amt

    def CalculateInterest(self):
        self.Interest=(self.Amount*BankAccount.ROI)/100
        return self.Interest
    
    def Display(self):
        print("Acount Holder Name:",self.Name)
        print("Current Balance :",self.Amount)


bobj1=BankAccount("Gaurav",100)
bobj1.Display() 
bobj1.Deposit(50)
bobj1.Display()
bobj1.withdraw(160)
Ret=bobj1.CalculateInterest()
print("Rate of Interest:",Ret)

bobj2=BankAccount("Sagar",500)
bobj2.Display() 
bobj2.Deposit(500)
bobj2.Display()
bobj2.withdraw(200)
bobj2.Display()
Ret=bobj2.CalculateInterest()
print("Rate of Interest:",Ret)

bobj3=BankAccount("Ram",0)
bobj3.Display() 
bobj3.Deposit(0)
bobj3.Display()
bobj3.withdraw(1)
bobj3.Display()
Ret=bobj3.CalculateInterest()
print("Rate of Interest:",Ret)

bobj4=BankAccount("Nandan",300)
bobj4.Display() 
bobj4.Deposit(100)
bobj4.Display()
bobj4.withdraw(0)
bobj4.Display()
Ret=bobj4.CalculateInterest()
print("Rate of Interest:",Ret)
