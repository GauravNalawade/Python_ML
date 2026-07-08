import threading

def EvenFactor(No):
    Sum=0
    for i in range(1,No+1):
        if No%i ==0 and i %2 ==0:
            print(i)
            Sum=Sum+i
    print("Sum of Even Factors:",Sum)

def OddFactor(No):
    Sum=0
    for i in range(1,No):
        if No%i ==0 and i %2 !=0:
            print(i)
            Sum=Sum+i
    print("Sum of Odd Factors:",Sum)


def main():
    print("Enter Number")
    no=int(input())


    tobj1=threading.Thread(target=EvenFactor,args=(no,))

    tobj2=threading.Thread(target=OddFactor,args=(no,))

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()

    print("Exit From Main")

if __name__=="__main__":
    main()



