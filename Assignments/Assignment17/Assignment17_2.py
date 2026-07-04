def DisplayPattern(No):
    for i in range(5):
        print()
        for i in range(5):
            print(" * ",end=" ")

def main():
    print("Enter Number:")
    no=int(input())

    DisplayPattern(no)

if __name__=="__main__":
    main()