def Display(Frequency):
    if Frequency<=0:
        print("Invalid Input")

    for i in range(1,Frequency+1):
        print("Jay Ganesh")

def main():
    Count=0
    print("Enter Frequency: ")
    Count=int(input())

    Display(Count)

if __name__=="__main__":
    main()
    
