import time
import multiprocessing
import os 

def SumEven(No):
    print(f"PID of SumEven:{os.getpid()} PPID of SumEven:{os.getppid()}")

    Sum=0
    for i in range(2,No,2):
        Sum=Sum+i
    print("Sum of Even:",Sum)


def SumOdd(No):
    print(f"PID of SumOdd:{os.getpid()} PPID of SumOdd:{os.getppid()}")
    Sum=0
    for i in range(1,No,2):
        Sum=Sum+i 
    print("Sum of Odd:",Sum)


def main():
    print(f"PID of Main:{os.getpid()} PPID of Main:{os.getppid()}")


    Start_Time=time.perf_counter()

    tobj1=multiprocessing.Process(target=SumEven,args=(100,))

    tobj2=multiprocessing.Process(target=SumOdd,args=(100,))

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()
    
    End_Time=time.perf_counter()

    print(f"Time Required is :{End_Time-Start_Time:.4f}")


if __name__=="__main__":
    main()