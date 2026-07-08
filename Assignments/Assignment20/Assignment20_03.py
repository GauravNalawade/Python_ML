import threading

def EvenList(Elements):
    Sum=0
    for i in Elements:
        if i %2 ==0:
            print(i)
            Sum=Sum+i
    print("Sum of Even Elements:",Sum)

def OddList(Elements1):
    Sum=0
    for i in Elements1:
        if i %2 !=0:
            print(i)
            Sum=Sum+i
    print("Sum of Odd Elements:",Sum)


def main():
    Data=[2,3,4,5,6,7,8,9,10]


    tobj1=threading.Thread(target=EvenList,args=(Data,))

    tobj2=threading.Thread(target=OddList,args=(Data,))

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()

    print("Exit From Main")

if __name__=="__main__":
    main()



