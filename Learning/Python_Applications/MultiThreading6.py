import threading
import time

def SumEven(No):
    Sum=0
    for i in range(2,No,2):
        Sum=Sum+i
    print("Sum of Even:",Sum)


def SumOdd(No):
    Sum=0
    for i in range(1,No,2):
        Sum=Sum+i
    print("Sum of Odd:",Sum)


def main():

    Start_Time=time.perf_counter()

    SumEven(10000000)
    SumOdd(10000000)

    End_Time=time.perf_counter()

    print(f"Time Required is :{End_Time-Start_Time:.4f}")


if __name__=="__main__":
    main()