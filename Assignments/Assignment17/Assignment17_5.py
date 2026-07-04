
def PrimeNum(No):
    if No <= 1:
        return False
    
    for i in range(2,No):
        if No % i == 0:
            return False
    return True

def main():
    print("Enter Number:")
    no=int(input())

    Ret=PrimeNum(no)
    if Ret==True:
        print("It is Prime Number")
    else:
        print("It is Not Prime Number")

if __name__=="__main__":
    main()
