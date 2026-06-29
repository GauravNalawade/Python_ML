def ReverseNumber(No):
    rev=0
    while(No != 0):
        rem=No % 10 
        rev=rev*10+rem
        No=No//10

    return rev

def main():
    print("Enter Number:")
    no=int(input())

    Ret=ReverseNumber(no)
    print("Reverse Number:",Ret)

if __name__=="__main__":
    main()