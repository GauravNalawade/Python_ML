def isPerfect(No):
    Sum=0
    for i in range(1,No):
        if No % i == 0:
            Sum=Sum+i
    return Sum

def main():

    print("Enter Number: ")
    no=int(input())

    Ret=isPerfect(no)

    if(Ret==no):
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

if __name__=="__main__":
    main()
