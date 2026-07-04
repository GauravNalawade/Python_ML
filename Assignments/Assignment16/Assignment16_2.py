def ChkNum(No):
    if No % 2 ==0:
        return True
    else:
        return False

def main():
    print("Enter Number: ")
    no=int(input())

    Ret=ChkNum(no)
    if Ret==True:
        print("Even Number")
    else:
        print("Odd Number")


if __name__=="__main__":
    main()