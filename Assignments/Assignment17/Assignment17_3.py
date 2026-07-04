def Factorial(No):
    Fact=1
    for i in range(1,No+1):
        Fact=Fact*i
    return Fact

def main():
    print("Enter Number:")
    no=int(input())

    Ret=Factorial(no)
    print(f"Factorial of {no} is:",Ret)
    
if __name__=="__main__":
    main()