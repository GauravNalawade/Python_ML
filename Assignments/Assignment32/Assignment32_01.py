import schedule
import time
import datetime

def CreateFile():
    Timestamp=datetime.datetime.now()
    CurrentTimestamp=Timestamp.strftime("%d_%m_%Y_%H_%M_%S")

    FileName=(f"File_{CurrentTimestamp}.txt")

    fobj=open(FileName,"w")

    fobj.write(f"FileName:{FileName}\n")
    fobj.write(f"Creation Date:{Timestamp.strftime("%d-%M-%Y")}\n")
    fobj.write(f"Creation time:{Timestamp.strftime("%H:%M:%S")}\n")

def main():
    schedule.every(1).minutes.do(CreateFile)
   
    while(True): 
        schedule.run_pending() 
        time.sleep(1)

if __name__=="__main__":
    main()