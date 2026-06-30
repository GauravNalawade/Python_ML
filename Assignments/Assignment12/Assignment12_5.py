def ReversePrint(No):
    for i in range(No,0,-1):
        print(i)
    
def main():
    print("Enter Number: ")
    no=int(input())

    print("Reverse Number")
    ReversePrint(no)

if __name__=="__main__": 
    main()