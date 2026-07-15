import threading
lock=threading.Lock()

Counter=0

def Thread1(no):
    global Counter
    for i in range(no):
        # lock.acquire()
        with lock:
            Counter+=1
        # lock.release()

def Thread2(no):
    global Counter
    for i in range(no):
        # lock.acquire()
        with lock:
            Counter+=1 
        # lock.release()

def Thread3(no):
    global Counter
    for i in range(no):
        # lock.acquire()
        with lock:
         Counter+=1
        # lock.release()

def main():

    tobj1=threading.Thread(target=Thread1,args=(900000,))
    tobj2=threading.Thread(target=Thread2,args=(900000,))
    tobj3=threading.Thread(target=Thread3,args=(900000,))
      
    tobj1.start()
    tobj2.start()
    tobj3.start()

    tobj1.join()
    tobj2.join()
    tobj3.join()

    print("Counter:",Counter)

if __name__=="__main__":
    main()


