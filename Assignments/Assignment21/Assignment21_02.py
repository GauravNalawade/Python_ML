import threading

def Maximum(Elements):
    Max=Elements[0]
    for i in Elements:
        if i > Max:
            Max=i
    print("Maximum Number From List is:",Max)

def Minimum(Elements):
    Min=Elements[0]
    for i in Elements:
        if i < Min:
            Min=i 
    print("Minimum Number From List is:",Min)

def main():
    Data=[]
    print("Enter the size of list:")
    size=int(input())

    for i in range(1,size+1):
        no=int(input())
        Data.append(no)
    
    tobj1=threading.Thread(target=Maximum,args=(Data,))

    tobj2=threading.Thread(target=Minimum,args=(Data,))

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()


if __name__=="__main__":
    main()

