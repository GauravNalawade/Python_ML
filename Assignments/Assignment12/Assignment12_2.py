def CheckFactors(No):
    for i in range(1,No+1):
        if No % i==0:
            print(i)

def main():
    print("Enter Number: ")
    no=int(input())

    CheckFactors(no)


if __name__=="__main__":
    main()