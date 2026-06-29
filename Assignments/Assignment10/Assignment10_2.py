def NaturalNoSum(No):
    Sum=0
    for i in range(1,No+1):
        Sum=Sum+i
    
    return Sum


def main():
    print("Enter Number: ")
    value=int(input())

    Ret=NaturalNoSum(value)
    print("Sum is: ",Ret)

if __name__=="__main__":
    main()