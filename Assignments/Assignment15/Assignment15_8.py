isNumDivisible = lambda No:((No % 3 == 0) and (No % 5 == 0))

def main():
    Data=[]

    print("Enter the Size of List:")
    Size=int(input())

    print("Enter Elements you want to insert")
    for i in range(Size):
        no=int(input())
        Data.append(no)

    print("Input Data is:",Data)

    FData=list(filter(isNumDivisible,Data))
    print("Data After Filter:",FData)

if __name__=="__main__":
    main()
