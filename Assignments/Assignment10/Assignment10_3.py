def Factorial(No):
    Fact=1
    for i in range(1,No+1):
        Fact=Fact*i
     
    return Fact


def main():
    print("Enter Number: ")
    value=int(input())

    Ret=Factorial(value)
    print(f"Factorial of {value} is: ",Ret)

if __name__=="__main__":
    main()