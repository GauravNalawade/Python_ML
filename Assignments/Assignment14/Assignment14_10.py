FindGreatest = lambda No1,No2,No3: No1 if(No1>No2 and No1>No3) else No2 if(No2>No1 and No2>No3) else No3

def main():
    print("Enter First Number: ")
    value1=int(input())

    print("Enter Second Number: ")
    value2=int(input())

    print("Enter Third Number: ")
    value3=int(input())

    Ret=FindGreatest(value1,value2,value3)
    print("Greatest Number is :",Ret)

if __name__=="__main__":
    main()

