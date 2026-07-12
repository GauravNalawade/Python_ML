import multiprocessing
import os

def CountOfEvenNum(No):
    Count=0
    for i in range(2,No+1,2):
        Count=Count+1

    print(f"""
    Process ID:{os.getpid()}
    Input Number:{No}
    Even Numbers Count:{Count}
          """)

    return Count
        
def main():
    Result=[]
    Data=[1000000,2000000,3000000,4000000]

    pobj=multiprocessing.Pool()
    Result=pobj.map(CountOfEvenNum,Data)

    pobj.close()
    pobj.join()

    print("Result is:")
    print(Result)


if __name__=="__main__":
    main()


    
    


