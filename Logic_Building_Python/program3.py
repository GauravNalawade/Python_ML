def Addition(No1,No2):
    Ans=No1+No2
    return Ans

def main():
    print("Enter First Number")
    value1=float(input())           #float

    print("Enter Second Number")
    value2=float(input())           #float

    Ret=Addition(value1,value2)
    print("Addition is: ",Ret)

if __name__=="__main__":
    main()