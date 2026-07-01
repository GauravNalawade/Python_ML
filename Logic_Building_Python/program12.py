def Display(Frequency):

    if Frequency<=0:
        print("Invalid Input")

    for i in range(2,Frequency+1,2):
        print(i,end=" ")

def main():
    Count=0
    print("Please Enter Frequency: ")
    Count=int(input())

    Display(Count)

if __name__=="__main__":
    main()
