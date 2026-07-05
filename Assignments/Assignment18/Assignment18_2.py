def Maximum(Elements):
   Max=Elements[0]
   for value in Elements:
        if value > Max:
            Max=value
   return Max
        
#   return max(Elements)

def main():
    Data=[]
    print("Enter Size of List:")
    Size=int(input())

    print("Enter Elements:")
    for i in range(Size):
        no=int(input())
        Data.append(no)
    
    Result=Maximum(Data)
    print("Maximum Number From List is:",Result)


if __name__=="__main__":
    main()