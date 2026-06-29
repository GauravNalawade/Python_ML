def Multable(No):
    for i in range(1,11):
        print(No*i)
    

def main():
    print("Enter Number: ")
    no=int(input())

    Multable(no)

if __name__=="__main__":
    main()