def ChkNum(No):
    if (No>0):
        print("Positive Number")
    elif(No<0):
        print("Negative Number")
    else:
        print("Zero")

def main():
    print("Enter Number:")
    no=int(input())

    Ret=ChkNum(no)

if __name__=="__main__":
    main() 