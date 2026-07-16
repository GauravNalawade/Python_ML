import threading

def Thread1(no):
    print("Numbers from 1 to 50")
    for i in range(1,no):
        print(i)

def Thread2(no):
   print("Numbers from 50 to 1")
   for i in range(no,0,-1):
        print(i)

def main():
    tobj1=threading.Thread(target=Thread1,args=(51,))

    tobj2=threading.Thread(target=Thread2,args=(50,))
      
    tobj1.start()
    tobj1.join()

    tobj2.start()
    tobj2.join()

if __name__=="__main__":
    main() 


