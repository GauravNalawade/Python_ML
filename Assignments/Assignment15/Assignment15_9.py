from functools import reduce
ProductOfElements = lambda No1,No2:No1*No2

def main():
    Data=[]
    print("Enter the Size of List:")
    Size=int(input())

    print("Enter the Elements you want to insert: ")
    for i in range(Size):
        no=int(input())
        Data.append(no)
    
    RData=reduce(ProductOfElements,Data)
    print("Data After Reduced: ",RData)


if __name__=="__main__":
    main()
