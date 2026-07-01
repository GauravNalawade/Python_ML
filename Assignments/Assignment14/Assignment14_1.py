Square=lambda No: No*No

def main():
    print("Enter Number: ")
    no=int(input())

    Ret=Square(no)    #no*no
    print(f"Square of {no} is: ",Ret)

if __name__=="__main__":
    main()

