from Arithmetic import *

def main():
    print("Enter First Number:")
    no1=int(input())

    print("Enter Second Number:")
    no2=int(input())

    Ret=Addition(no1,no2)
    print("Addition is:",Ret)

    Ret=Subtraction(no1,no2)
    print("Subtraction is:",Ret)

    Ret=Multiplication(no1,no2)
    print("Multiplication is:",Ret)

    Ret=Division(no1,no2)
    print("Division is:",Ret)

if __name__=="__main__":
    main()