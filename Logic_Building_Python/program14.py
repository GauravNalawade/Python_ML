# CheckPerfect Number
def CheckPerfect(No):
    Sum=0
    for i in range(1,No):
        if No % i == 0:
            Sum=Sum+i

    if(Sum==No):
        return True
    else:
        return False

def main():
    print("Enter Number: ")
    no=int(input())

    Ret=CheckPerfect(no)
    
    if(Ret==True):
        print(f"{no} is Perfect Number")
    else:
        print(f"{no} is Not a Perfect Number")

if __name__=="__main__":
    main()