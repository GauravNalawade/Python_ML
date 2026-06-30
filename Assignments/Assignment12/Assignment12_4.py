def PrintTillNumber(No):
    for i in range(1,No+1):
        print(i)

def main():
    print("Enter Number: ")
    no=int(input())

    PrintTillNumber(no)

if __name__=="__main__":
    main()  

