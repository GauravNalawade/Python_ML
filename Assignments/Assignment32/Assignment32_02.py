import schedule
import time
import datetime
import sys
import os

def GetFileSize(FilePath):
    Timestamp=datetime.datetime.now()
    CurrentTimestamp=Timestamp.strftime("%d_%m_%Y %I:%M:%S %p")

    if(os.path.exists(FilePath)==False):
        print("No such file path exists:",FilePath)
        return
    
    if(os.path.isfile(FilePath)==False):
        print("Given path is Not a File:",FilePath)
        return

    Size=os.path.getsize(FilePath)

    fobj=open("FileSizeLog.txt","a")

    fobj.write(f"File Path:{FilePath}\n")
    fobj.write(f"File size in bytes:{Size} bytes\n")
    fobj.write(f"Date and time: {CurrentTimestamp}\n")

    fobj.close()

def main():

    if (len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Automation Script is Used to GetFileSize")
            print("For Better usage please check --u flag")
            return
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Pease Run Script as")
            print("Python filename.py <FilePath>")
            print("FilePath should be Absolute path")
            return
        else:
            schedule.every(30).seconds.do(GetFileSize,sys.argv[1])
    else:
        print("Invalid Number of Arguments")

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()