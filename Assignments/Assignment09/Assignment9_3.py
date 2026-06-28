def Square(No):
    return No*No

def main():

    print("Enter Number : ")
    no=int(input())

    Ret=Square(no)
    print(f"Square of Number {no} is :",Ret)

if __name__=="__main__":
    main()