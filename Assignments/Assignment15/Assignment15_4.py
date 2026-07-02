from functools import reduce

Addition = lambda No1,No2: No1+No2

def main():
    Data=[]

    print("Enter the Size of List:")
    Size=int(input())

    print("Enter Elements you wan to insert:")
    for i in range(Size):
        no=int(input())
        Data.append(no)
    
    print("Input Data is:",Data)

    RData=reduce(Addition,Data)
    print("Data After Reduced:",RData)

if __name__=="__main__":
    main()