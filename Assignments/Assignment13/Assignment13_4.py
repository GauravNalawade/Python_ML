def ConvertBinary(No):
    binary=[]
    while(No != 0):
        binary.append(No%2)
        No=No//2

    for bit in reversed(binary):
        print(bit,end="")     
          
def main():

    print("Enter Number: ")
    no=int(input())
    ConvertBinary(no)

if __name__=="__main__":
    main()