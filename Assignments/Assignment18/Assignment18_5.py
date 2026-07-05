from MarvellousNum import ChkPrime

def ListPrime(Elements):
    Sum=0
    for value in Elements:
        if ChkPrime(value):
            Sum=Sum+value
    return Sum

def main():
    Data=[]
    print("Enter the Size of List")
    Size=int(input())

    print("Enter Elements of List:")
    for i in range(Size): 
        no=int(input())   
        Data.append(no)

    Ret=ListPrime(Data)
    print("Addition of Prime Number is:",Ret)


if __name__=="__main__":
    main()
