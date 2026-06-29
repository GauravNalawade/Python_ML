def OddNumber(No):
    for i in range(1,No+1):
        if ( i % 2 != 0):
            print(i)

def main():
    print("Enter Number: ")
    value=int(input())

    OddNumber(value)

if __name__=="__main__":
    main()