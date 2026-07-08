from functools import reduce

def ChkPrime(No):
    if No <=1:
        return False
    
    for i in range(2,No):
        if No % i ==0:
            return False
    return True
        
Multiply=lambda No: No*2

Maximum=lambda Elements1,Elements2: Elements1 if Elements1>Elements2 else Elements2

def main():
    Data=[]
    print("Enter the Size of list:")
    Size=int(input())

    print("Enter List Elements:")
    for i in range(Size):
        no=int(input())
        Data.append(no)
    
    print("Input List:",Data)
    
    Fdata=list(filter(ChkPrime,Data))
    print("Data After Filtered:",Fdata)

    Mdata=list(map(Multiply,Fdata))
    print("Data AFter Mapped:",Mdata)

    RData=reduce(Maximum,Mdata)
    print("Data After Reduced:",RData)

if __name__=="__main__":
    main()