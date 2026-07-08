import threading
import time

def Even():
    print("First 10 Even Numbers are :")
    for i in range(2,21,2):
        print(i,end=" ")
    print()

def Odd():
    print("First 10 Odd Numbers are :")
    for i in range(1,20,2):
        print(i,end=" ")
    print()

def main():

    start_time=time.perf_counter()

    tobj1=threading.Thread(target=Even)

    tobj2=threading.Thread(target=Odd)

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()

    print("Execution Completed")
    end_time=time.perf_counter()

    print(f"Time Required {end_time-start_time:.4f}")

if __name__=="__main__":
    main()