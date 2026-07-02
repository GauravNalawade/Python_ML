Square = lambda No : No * No 

def main():
    Data=[]

    print("Enter the Size of list: ")
    Size=int(input())
    
    print("Enter elements you want to Insert: ")
    for i in range(Size):
        no=int(input())
        Data.append(no)
    
    print("Input Data is: ",Data)

    MData=list(map(Square,Data))
    print("Data After Mapped: ",MData)


if __name__=="__main__":
    main()