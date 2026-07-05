def CountFrequency(Elements,No):
    count=0
    for value in Elements:
        if value==No:
            count=count+1
    return count

def main():
    Data=[]
    print("Enter Size of List")
    Size=int(input())

    print("Enter Elements of List:")
    for i in range(Size):
        no=int(input())
        Data.append(no)
    
    print("Enter Element To Search:")
    search=int(input())

    Ret=CountFrequency(Data,search)
    print(f"Frequency Count of {search} in List is:",Ret)

if __name__=="__main__":
    main()