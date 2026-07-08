from functools import reduce

ChkEVen=lambda no: no % 2==0

CalSquare=lambda No: No*No

Sum=lambda Elements1,Elements2: Elements1+Elements2

def main():
    Data=[]
    print("Enter the Size of list:")
    Size=int(input())

    print("Enter List Elements:")
    for i in range(Size):
        no=int(input())
        Data.append(no)
    
    print("Input List:",Data)
    
    Fdata=list(filter(ChkEVen,Data))
    print("Data After Filtered:",Fdata)

    Mdata=list(map(CalSquare,Fdata))
    print("Data AFter Mapped:",Mdata)

    RData=reduce(Sum,Mdata)
    print("Data After Reduced:",RData)


if __name__=="__main__":
    main()