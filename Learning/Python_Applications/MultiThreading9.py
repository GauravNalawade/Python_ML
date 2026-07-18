import threading
import time

def SumEven(No):
    print("TID of Sum Even Thread is:",threading.get_ident())

def SumOdd(No):
    print("TID of Sum Odd Thread is:",threading.get_ident())
  

def main():
    print("TID of Main Thread is:",threading.get_ident())

    Start_Time=time.perf_counter()

    tobj1=threading.Thread(target=SumEven,args=(100000000,))

    tobj2=threading.Thread(target=SumOdd,args=(100000000,))

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()
    
    End_Time=time.perf_counter()

    print(f"Time Required is :{End_Time-Start_Time:.4f}")


if __name__=="__main__":
    main()