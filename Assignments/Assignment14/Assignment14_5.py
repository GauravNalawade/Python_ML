CheckEven = lambda No: No % 2 == 0

def main():
    print("Enter Number: ")
    no=int(input())

    Ret=CheckEven(no)
    print(Ret)

if __name__=="__main__":
    main()