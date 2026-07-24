import schedule
import time
import sys
import os

def DisplayedFileContents(FilePath):

    if (os.path.exists(FilePath)==False):
        print("No such File Path exists") 
        return

    if(os.path.isfile(FilePath)==False):
        print("File Does Not Exist:",FilePath)
        return 
 
    try:
        fobj=open(FilePath,"r")
        Data=fobj.read()
  
        if(Data==""):
            print("File is Empty")
        else:
            print(Data)

    except PermissionError as pobj:
        print("Permission is denied:",pobj)

    except OSError as e:
        print("File cannot be opened:",e)

def main():
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Script is used to DisplayedFileContents")
            print("For Better use please check --u")
            return
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Please run script as")
            print("python fileName.py <FilePath>")
            print("FilePath should be Absolute path")
            return
        else:
            schedule.every(1).minutes.do(DisplayedFileContents,sys.argv[1])
    else:
        print("Invalid Number of Arguments")

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
 
