def Addition(Elements):
    Sum=0
    for i in Elements:
        Sum=Sum+i
    return Sum

def main():
    Data=[]
    print("Enter the Size of List")
    Size=int(input())

    print("Enter the Number:")
    for i in range(Size):
        no=int(input())
        Data.append(no)

    Result=Addition(Data)
    print("Addition of All Elements is:",Result)
    

if __name__=="__main__":
    main()

    
