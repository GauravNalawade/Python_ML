isDivisible = lambda No: No % 5 == 0

def main():
    print("Enter Number")
    no=int(input())

    Ret=isDivisible(no)
    print(Ret)

if __name__=="__main__":
    main()

