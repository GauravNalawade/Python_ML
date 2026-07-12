import multiprocessing
import time

def ChkExpression(No):
    Sum=0
    for i in range(1,No+1):
        Sum=Sum+i**5
    return Sum

def main():
    Result=[]
    Data=[1000000,2000000,3000000,4000000]
   
    start_time=time.perf_counter()

    pobj=multiprocessing.Pool()
    Result=pobj.map(ChkExpression,Data)
    
    pobj.close()
    pobj.join()
    
    end_time=time.perf_counter()

    print("Result is:")
    print(Result)

    print(f"Execution Time is:{end_time-start_time:.4f} Seconds")

if __name__=="__main__":
    main()

