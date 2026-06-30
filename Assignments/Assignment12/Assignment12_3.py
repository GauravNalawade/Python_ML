def Arithmatic(No1,No2):
    Addition= No1+No2
    print("Addition is: ",Addition)

    Subtraction= No1-No2
    print("Substraction is: ",Subtraction)

    Multiplication=No1*No2
    print("Multiplication is: ",Multiplication)

    Division=No1/No2
    print("Division is: ",Division)

def main():
    print("Enter First Number: ")
    no1=int(input())

    print("Enter Second Number: ")
    no2=int(input())

    Arithmatic(no1,no2)

if __name__=="__main__":
    main()