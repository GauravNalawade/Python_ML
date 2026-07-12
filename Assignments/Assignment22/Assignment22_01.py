import multiprocessing
import os

def SumOfSquare(No):
    print("Process is Running with PID:",os.getpid())
    
    Sum=0
    for i in range(1,No+1):
            Square=i*i
            Sum=Sum+Square
    return Sum

def main():
    Data=[1000000,2000000,3000000,4000000]
    Result=[]

    pobj=multiprocessing.Pool()
    Result=pobj.map(SumOfSquare,Data)

    pobj.close()
    pobj.join()

    print("Result is:")
    print(Result)
    
if __name__=="__main__":
    main()