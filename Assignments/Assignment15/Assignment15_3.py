CheckEvenNum = lambda No:(No % 2 != 0)

def main():
    Data=[]

    print("Enter the Size of List:")
    Size=int(input())

    print("Enter Elements you want to insert")
    for i in range(Size):
        no=int(input())
        Data.append(no)

    print("Input Data is:",Data)

    FData=list(filter(CheckEvenNum,Data))
    print("Data After Filter:",FData)

if __name__=="__main__":
    main()
