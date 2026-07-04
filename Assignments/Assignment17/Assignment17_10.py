def SumOfDigit(No):
    Sum=0
    while(No !=0):
        rem=No%10
        Sum=Sum+rem
        No=No//10
        
    return Sum

def main():
    print("Enter Number:")
    no=int(input())

    Ret=SumOfDigit(no)
    print(f"Sum of Digit in {no} is:",Ret)

if __name__=="__main__":
    main()