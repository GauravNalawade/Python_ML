# ////////////////////////////////////////////////////////////
# //
# //  Function Name : AdditionTwoNumbers
# //  Description :   It is used to perform addition 
# //  Input :         Int,Int
# //  Output:         Int
# //  Author:         Gaurav Nalawade 
# //  Date:           01/07/2026
# //
# //////////////////////////////////////////////////////////
def Addition(No1,No2):
    Add=0.0

    if(No1<0.0):
        No1=-No1
    if(No2<0.0):
        No2=-No2
    Add=No1+No2
    return Add

# //////////////////////////////////////////////////////////
# //Entry point function for application
# //////////////////////////////////////////////////////////
def main():
    print("Enter First Number")
    value1=float(input())

    print("Enter Second Number")
    value2=float(input())

    Ret=Addition(value1,value2)
    print("Addition is: ",Ret)

if(__name__=="__main__"):
    main()

# //////////////////////////////////////////////////////////
# //Test cases successfully handeled by the Application 
# //
# // input:10.5   input:3.2     output:13.7
# // input:-10.5  input:3.2     output:13.7
# // input:10.5   input:-3.2    output:13.7
# // input:-10.5  input:-3.2    output:13.7
# // input:10.5   input:0.0     output:10.5
# //
# //////////////////////////////////////////////////////////