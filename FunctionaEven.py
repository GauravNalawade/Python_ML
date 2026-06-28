CheckEven = lambda No1: (No1 % 2==0)
     
def main():
    Value=int(input("Enter Number: "))
    Ret=CheckEven(Value)       #Ret=(value % 2==0)

    if Ret==True:                      
        print("It is Even Number")  
    else:
        print("It is Odd Number")  

if __name__=="__main__":
    main()
