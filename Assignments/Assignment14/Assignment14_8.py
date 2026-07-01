Addition = lambda No1,No2: No1+No2

def main():
    print("Enter First Number: ")
    no1=int(input())

    print("Enter Second Number: ")
    no2=int(input())

    Ret=Addition(no1,no2)
    print("Addition is: ",Ret)

if __name__=="__main__":
    main()
