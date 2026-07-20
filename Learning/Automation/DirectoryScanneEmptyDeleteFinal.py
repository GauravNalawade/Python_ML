####################################################################
#
# Importing Required Libraries
#
####################################################################

import sys
import os
import time
import schedule

####################################################################
#
# Function Name : DirectoryScanner
# Input:          Name of Directory
# Description:    Delete all empty files periodically
# Date:           19/07/1026
# Author:         Gaurav Sunil Nalawade
#
####################################################################


def DirectoryScanner(DirectoryPath):
    Border="-"*40
    timestamp = time.ctime()
    LogFileName="Marvellous%s.log"%(timestamp)
    LogFileName=LogFileName.replace(" ","_")
    LogFileName=LogFileName.replace(":","_")

    Ret=False
    Ret=os.path.exists(DirectoryPath)
    
    if(Ret==False):
        print("Marvellous Automation Error: There is no such Directory with name",DirectoryPath)
        return 
    
    Ret=os.path.isdir(DirectoryPath)

    if(Ret==False):
        print("Marvellous Automation Error: It is not a Directory with name",DirectoryPath)
        return


    print("Log file gets created with Name:",LogFileName)

    fobj=open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write("Marvellous AutomationScript \n")
    fobj.write(Border+"\n\n")
    

    fobj.write("File from the directory are:\n\n")
    fobj.write(Border+"\n")

    TotalFiles=0
    EmptyFiles=0

    for FolderName,SubFolder,FileName in os.walk(DirectoryPath):
        for fname in FileName:
            TotalFiles=TotalFiles+1

            fname =os.path.join(FolderName,fname)
            fobj.write(fname+":"+os.path.getsize(fname)+"bytes \n")

            if(os.path.getsize(fname)==0):
                EmptyFiles=EmptyFiles+1 
                os.remove(fname)

    fobj.write(Border+"\n")
    fobj.write("Total files Scanned:"+TotalFiles+"\n")
    fobj.write("Total Empty file found and Deleted:"+EmptyFiles+"\n")

    fobj.write(Border+"\n")
    fobj.write("Log file gets Creates at:"+timestamp)
    fobj.write("\n"+Border+"\n")

    fobj.close()

####################################################################
#
# Function Name : main
# Input:          Command line arguments
# Description:    It control the script
# Date:           19/07/1026
# Author:         Gaurav Sunil Nalawade
#
####################################################################
def main():
    Border="-"*40
    print(Border)
    print("Marvellous AutomationScript")
    print(Border)
    if (len(sys.argv) ==2):
        if (sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Automation Script is used to travel the directory")
            print("for better usage please check --u flag")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Please execute the script as")
            print("Python FileName.py DirectoryName")
            print("Directory Name should be Absolute path")
        else:
            # DirectoryScanner(sys.argv[1])

            schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])

            while(True):
                schedule.run_pending()
                time.sleep(1)
    else:
        print("Invalid Number of Arguments")
        print("Please use --h or --u for more information")

    print(Border)
    print("THank you for uing Marvellous AutomationScript")
    print(Border)

####################################################################
#
# Starter of the Automation script
#
####################################################################
if __name__=="__main__":
    main()  