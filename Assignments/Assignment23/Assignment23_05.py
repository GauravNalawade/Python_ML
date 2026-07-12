import multiprocessing
import os

def Factorial(No):
    Fact=1
    for i in range(1,No+1):
        Fact=Fact*i

    print(f"""
    Process ID   : {os.getpid()}
    Input Number : {No}
    Factorial    : {Fact}
    """)
    return Fact

def main():
    Data=[10,15,20,25]
    Result=[]

    pobj=multiprocessing.Pool()
    Result=pobj.map(Factorial,Data)

    pobj.close()
    pobj.join()

    print(Result)

if __name__=="__main__":
    main()