Cube=lambda No: No*No*No

def main():

    print("Enter Number: ")
    no=int(input())

    Ret=Cube(no)
    print(f"Cube of {no} is :",Ret)

if __name__=="__main__":
    main()