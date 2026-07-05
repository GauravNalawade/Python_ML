import time 
def Factorial(No):
    Fact=1
    for i in range(1,No+1):
        Fact=Fact*i
    return Fact


def main():
    Value=int(input("Enter Number:"))

    Start_Time=time.time()
    Ret=Factorial(Value)
    End_Time=time.time()

    print(f"Factorial of {Value} is {Ret}")
    print(f"Time period is: {End_Time-Start_Time} seconds")
    


if __name__=="__main__":
    main()