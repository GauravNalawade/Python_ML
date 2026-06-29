def CountDigit(No):
    Count=0
    while(No != 0):
        No=No//10
        Count=Count+1
    return Count

def main():
    print("Enter Number: ")
    no=int(input())

    Ret=CountDigit(no)
    print("Number of Digit: ",Ret)


if __name__=="__main__":
    main()