import schedule
import sys
import time
import datetime
import shutil
import os

def BackUp(SourceFilePath,DestinationDirPath):
    
    if(os.path.exists(SourceFilePath)==False):
        print("SourceFile Path Doesn't exist")
        return 
     
    DateTime=datetime.datetime.now()

    CurrentDateTime=DateTime.strftime("%d-%m-%Y %H:%M:%S")
    BackFileName="Data_%s.txt"%(CurrentDateTime)   
    BackFileName=BackFileName.replace(":","_")
    BackFileName=BackFileName.replace(" ","_")  
    BackFileName=BackFileName.replace("-","_")


    FormmatedDTime=DateTime.strftime("%d-%m-%Y %I:%M:%S %p")
    fobj=open("backup_log_.txt","a")
    fobj.write(f"Backup Completed successfully at {FormmatedDTime}\n")

    shutil.copy(SourceFilePath,DestinationDirPath)

    
def main():
    schedule.every(5).seconds.do(BackUp,sys.argv[1],sys.argv[2])

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()



