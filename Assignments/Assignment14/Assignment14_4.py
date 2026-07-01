Minimum= lambda No1,No2: No1<No2

def main(): 
    print("Enter First Number: ")
    value1=int(input())

    print("Enter Second Number: ")
    value2=int(input())

    Ret=Minimum(value1,value2)
    if(Ret==True):
        print(f"Minimum Number between {value1} and {value2} is: ",value1)
    else :
        print(f"Minimum Number between {value1} and {value2} is: ",value2)

if __name__=="__main__":
    main()