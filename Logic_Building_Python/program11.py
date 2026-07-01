def Display(Frequency):

    if Frequency<=0:
        print("Invalid Input")

    for i in range(Frequency,0,-1): #print in reverse order
        print(i,end=" ")

def main():
    Count=0
    print("Enter Frequency: ")
    Count=int(input())

    Display(Count)

if __name__=="__main__":
    main()
    
