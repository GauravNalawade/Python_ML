def Minimum(Elements):
   Min=Elements[0]
   for value in Elements:
        if value < Min:
            Min=value
   return Min
        
#   return min(Elements)

def main():
    Data=[]
    print("Enter Size of List:")
    Size=int(input())

    print("Enter Elements:")
    for i in range(Size):
        no=int(input())
        Data.append(no)
    
    Result=Minimum(Data)
    print("Minimum Number From List is:",Result)


if __name__=="__main__":
    main()