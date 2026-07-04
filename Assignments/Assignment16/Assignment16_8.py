def NumofStar(No):
    # print(" * "*5) 
    for i in range(No):
        print(" * ",end=" ")

def main():
    print("Enter Number:")
    no=int(input())
    
    NumofStar(no)

if __name__=="__main__":
    main()