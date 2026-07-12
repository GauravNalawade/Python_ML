import multiprocessing
import os

def SumOfEvenNum(No):
    Sum=0
    for i in range(2,No+1,2):
        Sum=Sum+i

    print(f"""
    Process ID:{os.getpid()}
    Input Number:{No}
    Sum of Even Numbers:{Sum}
          """)

    return Sum
        
def main():
    Result=[]
    Data=[1000000,2000000,3000000,4000000]

    pobj=multiprocessing.Pool()
    Result=pobj.map(SumOfEvenNum,Data)

    pobj.close()
    pobj.join()

    print("Result is:")
    print(Result)


if __name__=="__main__":
    main()


    
    


