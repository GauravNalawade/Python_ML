import schedule
import time
import datetime


def Display():
    fobj=open("Marvellous.txt","a")

    CurrentDatetime=datetime.datetime.now()
    Data=(f"Task executed at:{CurrentDatetime.strftime("%d-%m-%Y %I:%M:%S:%p")}\n")

    fobj.write(Data) 

def main():
    schedule.every(5).minutes.do(Display)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()