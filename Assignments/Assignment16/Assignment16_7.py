def isDividibleBy5(No):
    if No % 5 == 0:
        return True
    else:
        return False
    
def main():
    print("Enter Number:")
    no=int(input())

    Ret=isDividibleBy5(no)
    print(Ret)

if __name__=="__main__":
    main()