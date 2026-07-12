import multiprocessing

def isPrimeNumber(No):
    if No <=1:
        return False
    
    for i in range(2,No):
        if No % i == 0:
            return False
    return True

def ChkPrimeCount(No):
    Count=0
    for i in range(2,No+1):
        if isPrimeNumber(i):
            Count=Count+1
    return Count

def main():
    Result=[]
    Data=[10000,20000,30000,40000]

    pobj=multiprocessing.Pool()

    Result=pobj.map(ChkPrimeCount,Data)
    
    pobj.close()
    pobj.join()

    print("Result is:")
    print(Result)

if __name__=="__main__":
    main()

