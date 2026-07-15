import threading

def isPrime(No):
        if No<=1:
            return False
        for i in range(2,No):
            if No % i == 0:
                return False
        return True

def PrintPrime(ELements):
     print("Prime Numbers")
     for i in ELements:
          if (isPrime(i)):
               print(i)

def NonPrime(Elements):
     print("Non Prime Numbers")
     for i in Elements:
          if(isPrime(i)==False):
                print(i)

def main():
    Data=[1,2,3,5,7,11,12]

    tobj1=threading.Thread(target=PrintPrime,args=(Data,))
    tobj2=threading.Thread(target=NonPrime,args=(Data,))
    
    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()

if __name__=="__main__":
    main();

