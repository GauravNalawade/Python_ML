import sys
import os
import time

def DirectoryScanner(DirectoryPath):
    timestamp = time.ctime()
    LogFileName="Marvellous%s.log"%(timestamp)
    LogFileName=LogFileName.replace(" ","_")
    LogFileName=LogFileName.replace(":","_")

    print("Log file gets created with Name:",LogFileName)

    fobj=open(LogFileName,"w")

    fobj.write("Marvellous AutomationScript \n")

    fobj.write("File from the directory are:\n")

    for FolderName,SubFolder,FileName in os.walk(DirectoryPath):
        for fname in FileName:
            fobj.write(fname+"\n")

    fobj.close()

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
            DirectoryScanner(sys.argv[1])
    else:
        print("Invalid Number of Arguments")
        print("Please use --h or --u for more information")

    print(Border)
    print("THank you for uing Marvellous AutomationScript")
    print(Border)


if __name__=="__main__":
    main()