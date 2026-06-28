def Multiplication(No1,No2):
    Ans=0
    Ans=No1*No2
    return Ans

def main():
    print("Enter First Number")
    value1=int(input())

    print("Enter Second Number")
    value2=int(input())

    Ret=Multiplication(value1,value2)
    print("Multiplication is : ",Ret)

if __name__=="__main__":
    main()