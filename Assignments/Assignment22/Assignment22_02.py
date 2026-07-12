import multiprocessing
import os

def Factorial(No):
    print("Process PID:",os.getpid())

    Fact=1
    for i in range(1,No+1):
        Fact=i*Fact 

    print("Input Number:",i)
    print("Factorial:",Fact)
    print()
    return Fact

def main():
    Data=[10,15,20,25]
    Result=[]

    pobj=multiprocessing.Pool()
    Result=pobj.map(Factorial,Data)
    
    pobj.close()
    pobj.join()

    print("Result is")
    print(Result)

if __name__=="__main__":
    main()