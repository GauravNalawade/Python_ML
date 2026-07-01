# ////////////////////////////////////////////////////////////
# //
# //  Function Name : CheckEvenOdd
# //  Description :   It is used to check whether number is Even or Odd
# //  Input :         Integer
# //  Output:         boolean
# //  Author:         Gaurav Nalawade 
# //  Date:           01/07/2026
# //
# //////////////////////////////////////////////////////////
def CheckEvenOdd(No):
    if No % 2 == 0:
        return True
    else:
        return False
# //////////////////////////////////////////////////////////
# //Entry point function for application
# //////////////////////////////////////////////////////////
def main():
    print("Enter Number: ")
    value=int(input())
    
    Ret=CheckEvenOdd(value)

    if(Ret==True):
        print(f"{value} is Even Number")
    else:
        print(f"{value} is Odd Number")

if __name__=="__main__":
    main()
