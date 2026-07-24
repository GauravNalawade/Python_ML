import schedule
import time
import sys
import os
import shutil
import datetime

def CopyTextFiles(SourceDirectoryPath,DestinationDirectoryPath):

    if (os.path.exists(SourceDirectoryPath)==False):
        print("No such Directory Path exists:",SourceDirectoryPath)
        return
    if(os.path.isdir(SourceDirectoryPath)==False):
        print("There is no such Directory with Name:",SourceDirectoryPath)
        return 
    
    if (os.path.exists(DestinationDirectoryPath)==False):
        print("No such Directory path exists:",DestinationDirectoryPath)  
        return 
    if (os.path.isdir(DestinationDirectoryPath)==False):
        print("There is no such Directory with Name",DestinationDirectoryPath)
        return

    for FolderName,SubFolderName,FileName in os.walk(SourceDirectoryPath):
        for Fname in FileName:
            FullPath=os.path.join(FolderName,Fname)
            if(FullPath.lower().endswith(".txt")):
                try:
                    shutil.copy(FullPath,DestinationDirectoryPath)
                    fobj=open("CopiedFileLogs.log","a")
                    fobj.write(f"File Copied:{FullPath} :{datetime.datetime.now()}\n")
                    fobj.close()
                except Exception as e:
                    print("Unable to copy file:",FullPath)
                    print("Error:",e)

def main():
    if(len(sys.argv)==3):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Script is used to Copies all .txt files from one directory to another Directiry")
            print("For Better use please check --u")
            return
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Please run script as")
            print("python fileName.py <SourceDirectoryPath> <DestinationDirectoryPath>")
            print("DirectoryPath should be Absolute path")
            return
        else:
            schedule.every(10).minutes.do(CopyTextFiles,sys.argv[1],sys.argv[2])
    else:
        print("Invalid Number of Arguments")
        return

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
 
