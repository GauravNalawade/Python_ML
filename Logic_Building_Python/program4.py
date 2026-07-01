def Addition(No1,No2):

    # Updater
    if(No1<0):
        No1=-No1
    if(No2<0):
        No2=-No2

    Add=No1+No2
    return Add

def main():
    print("Enter First Number")
    value1=int(input())           

    print("Enter Second Number")
    value2=int(input())           

    Ret=Addition(value1,value2)
    print("Addition is: ",Ret)

if __name__=="__main__":
    main()