import schedule
import datetime
import time

def CreateLogFile():
      
    DateTime=datetime.datetime.now()
    FormattedDateTime = DateTime.strftime("%d-%m-%Y %H:%M:%S")

    LogFileName="MarvellousLog_%s.txt"%(FormattedDateTime)
    LogFileName=LogFileName.replace(" ","_")
    LogFileName=LogFileName.replace(":","_")
    LogFileName=LogFileName.replace("-","_")


    CreationTime=DateTime.strftime("%d-%m-%Y %I:%M:%S %p")

    fobj=open(LogFileName,"w")

    fobj.write("Log file created successfully.\n")
    fobj.write(f"Creation Time:{CreationTime}")

def main():
    schedule.every(10).minutes.do(CreateLogFile)

    while(True):
        schedule.run_pending()
        time.sleep(1)


if __name__=="__main__":
    main() 
