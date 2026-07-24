import schedule
import time
import sys
import os
import shutil
import datetime

def CopyFiles(SourceFilePath,DestinationDirectoryPath):

    if (os.path.exists(SourceFilePath)==False):
        print("No such Path exists:",SourceFilePath)
        return
    if(os.path.isfile(SourceFilePath)==False):
        print("There is no such File with Name:",SourceFilePath)
        return 
    
    if (os.path.exists(DestinationDirectoryPath)==False):
        print("No such path exists:",DestinationDirectoryPath)  
        return 
    if (os.path.isdir(DestinationDirectoryPath)==False):
        print("There is no such Directory with Name",DestinationDirectoryPath)
        return
    
    CurrentDateTime=datetime.datetime.now()


    BackUpTimeStamp=CurrentDateTime.strftime("%d_%m_%Y_%H_%M_%S") 

    BackUpFileName=(f"Data_{BackUpTimeStamp}.txt")

    BackupFilePath=os.path.join(DestinationDirectoryPath,BackUpFileName)
 
    try:
        shutil.copy(SourceFilePath,BackupFilePath)

        FormattedDateTime=CurrentDateTime.strftime("%d-%m-%Y %I:%M:%S %p")

        fobj=open("backup_log.txt","a")
        fobj.write(f"Backup completed successfully at {FormattedDateTime}\n")
        fobj.close()
    except Exception as e:
            print("Unable to copy file:",FullPath)
            print("Error:",e)

def main():
    if(len(sys.argv)==3):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Script is used to Copy the source file to the destination directory.")
            print("For Better use please check --u")
            return 
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):    
            print("Please run script as")
            print("python fileName.py <SourceFilePath> <DestinationDirectoryPath>")
            print("DirectoryPath should be Absolute path")
            return
        else:
            schedule.every(1).hours.do(CopyFiles,sys.argv[1],sys.argv[2])
    else:
        print("Invalid Number of Arguments")
        return

    while(True): 
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()