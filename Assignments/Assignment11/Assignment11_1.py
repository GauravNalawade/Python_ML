def isPrime(No):
    if No <= 1:
        return False

    for i in range(2,No):
        if No % i ==0:
            return False
        
    return True


def main():
    print("Enter Number: ")
    value=int(input())

    Ret=isPrime(value)
    
    if Ret== True:
        print(f"{value} is Prime Number")
    else:
        print(f"{value} is Not a Prime Number")


if __name__=="__main__":
    main()

    
            
            


