from functools import reduce

chkGreater=lambda value: value>=70 and value<=90

Increase=lambda No: No+10

Sum=lambda Elements1,Elements2: Elements1*Elements2

def main():
    Data=[]
    print("Enter the Size of list:")
    Size=int(input())

    print("Enter List Elements:")
    for i in range(Size):
        no=int(input())
        Data.append(no)
        
    print("Input List:",Data)
    
    Fdata=list(filter(chkGreater,Data))
    print("Data After Filtered:",Fdata)

    Mdata=list(map(Increase,Fdata))
    print("Data AFter Mapped:",Mdata)

    RData=reduce(Sum,Mdata)
    print("Data After Reduced:",RData)


if __name__=="__main__":
    main()