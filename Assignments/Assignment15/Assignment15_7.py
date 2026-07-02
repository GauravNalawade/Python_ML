CheckStrLen= lambda String: len(String)>5

def  main():
    Data=[]
    print("Enter the Size of List")
    Size=int(input())

    print("Enter the Strings :")
    for i in range(Size):
        word=input()
        Data.append(word)

    print("Input Data is:",Data)
    FData=list(filter(CheckStrLen,Data))
    print("Data After Filter:",FData)

if __name__=="__main__":
    main()


    


