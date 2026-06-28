def ChkGreater(No1,No2):
    if(No1>No2):
        return True,No1
    else:
        return False,No2

def main():

    print("Enter First Number: ")
    Value1=int(input())

    print("Enter Second Number: ")
    Value2=int(input())

    Ret1,Ret2=ChkGreater(Value1,Value2)

    if Ret1==True:
        print(Ret2,"is greater")
    else:
        print(Ret2,"is greater")
        

if __name__=="__main__":
    main()