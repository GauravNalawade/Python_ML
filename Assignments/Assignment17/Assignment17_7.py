def PatterPrint(No):
    for i in range(1,No+1):
        for j in range(1,No+1):
            print(j,end=" ")
        print()

def main():
    print("Enter Number:")
    no=int(input())

    PatterPrint(no)

if __name__=="__main__":
    main()

