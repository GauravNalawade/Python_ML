def SumOfFactors(No):
    Sum=0
    for i in range(1,No//2+1):
        if No % i == 0:
            Sum=Sum+i;
    return Sum

def main():
    print("Enter Number:")
    no=int(input())

    Ret=SumOfFactors(no)
    print("Sum of Factors:",Ret)

if __name__=="__main__":
    main()
