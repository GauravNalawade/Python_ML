def CheckDivisible(No):
    if (No % 3 == 0 and No % 5 == 0):
        return True
    else:
        return False

def main():
    print("Enter Number: ")
    no=int(input())

    Ret=CheckDivisible(no)

    if Ret ==True:
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

if __name__=="__main__":
    main()