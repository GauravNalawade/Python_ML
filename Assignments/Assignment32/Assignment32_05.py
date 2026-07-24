import schedule
import time
import sys
import os
import datetime

def DeleteAllEmptyFiles(DirectoryPath): 

    if (os.path.exists(DirectoryPath)==False):
        print("No such Directory Path exists:",DirectoryPath)
        return
    if(os.path.isdir(DirectoryPath)==False):
        print("There is no such Directory with Name:",DirectoryPath)
        return 
   
    for FolderName,SubFolderName,FileName in os.walk(DirectoryPath):
        for Fname in FileName:
            FullPath=os.path.join(FolderName,Fname)
            try:
                if(os.path.getsize(FullPath)==0):
                    os.remove(FullPath)
                    fobj=open("DeleteFiles.log","a")
                    fobj.write(f"Deleted File:{FullPath} :{datetime.datetime.now()}\n")
                    fobj.close()
            except PermissionError as pobj:
                print("Permission is denied:",pobj)

def main():
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Script is used to deletes All Empty files from specified Directiry")
            print("For Better use please check --u")
            return
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Please run script as")
            print("python fileName.py <DirectoryPath>")
            print("DirectoryPath should be Absolute path")
            return
        else:
            schedule.every(5).seconds.do(DeleteAllEmptyFiles,sys.argv[1])
    else:
        print("Invalid Number of Arguments")
        return

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
 
