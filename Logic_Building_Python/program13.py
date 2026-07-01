# Factors of Number 
def FactorsOfNumber(No):
    for i in range(1,No//2+1):
        if No % i == 0:
            print(i)
    # print(No)   

def main():
    print("Enter Number")
    no=int(input())

    FactorsOfNumber(no)

if __name__=="__main__":
    main()