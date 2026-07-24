import schedule
import sys
import time
import os
import datetime

def CountFiles(DirectoryPath): 
   
    Ret=False
    
    Ret=os.path.exists(DirectoryPath)

    if (Ret==False):
        print("There is no such Directory with Name:",DirectoryPath)
        return 

    Ret=os.path.isdir(DirectoryPath)

    if (Ret==False):
        print("It is not a directory with Name:",DirectoryPath)  
        return
     
    CurrentDateTime=datetime.datetime.now()
    CurrentTime=CurrentDateTime.strftime("%d-%m-%Y %I:%M:%S %p") 

    TotalFiles=0
    fobj=open("DirectoryCountingLog.txt","a")

    fobj.write(f"Directory Path:{DirectoryPath}\n") 

    for FolderName,SubFolder,FileName in os.walk(DirectoryPath):

        for fnname in FileName:
            TotalFiles +=1

    fobj.write(f"Number of files:{TotalFiles}\n")
    fobj.write(f"Date and Time:{CurrentTime}\n")
    
def main():

    if(len(sys.argv)==2):

        if(sys.argv[1]== "--h" or sys.argv[1]=="--H"):
            print("This Automation Script is used to Count No of Files and SubDirectories")
            print("For Better usage please check --u flag")
            return

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Please Execute the script as")
            print("python FileName.py <DirectoryName>")
            print("Directory should be absolute path")
            return
        
        else:
            schedule.every(5).minutes.do(CountFiles,sys.argv[1])
    
        while(True):
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid Number of arguments")
        print("please use --h or --u for more information")

if __name__=="__main__":
    main()

