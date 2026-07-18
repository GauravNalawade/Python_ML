from Marvellous import Addition

def main():
    print("Enter First Number:")
    value1=int(input())

    print("Enter Second Number:")
    value2=int(input())

    Ret=Addition(value1,value2)    

    print("Addition is :",Ret)

    Ret=Substraction(value1,value2)

    print("Substraction is :",Ret) #Error



if __name__=="__main__":
    main()