
CheckEvenCount = lambda No: No%2==0


def main():
    Data=[]
    print("Enter Size of List: ")
    Size=int(input())

    print("Enter Elements of List: ")
    for i in range(Size):
        no=int(input())
        Data.append(no)

    print("Input Data are: ",Data)

    FData=list(filter(CheckEvenCount,Data))
    print("Data After Filtered:", FData)

    print("Count of Even Numbers:",len(FData))

if __name__=="__main__":
    main()