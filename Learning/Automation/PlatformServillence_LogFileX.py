import psutil
import sys
import os 
import time

def PlatformSurvillance(FolderName):
    Border="-"*50

    Ret=False

    Ret=os.path.exists(FolderName)

    if(Ret==True):
        Ret=os.path.isdir(FolderName)
        if(Ret==False):
            print("Unable to processed as Directoyr name is existing but its not a directory")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for the logfile gets created successfully ")

    timestamp=time.strftime("%Y-%M-%d_%H-%M-%S")

    FileName=os.path.join(FolderName,"Marvellous_%s.log"%timestamp)

    fobj=open(FileName,"w")

    print(f"Log file gets successfully created with name {FileName}")

def main():

    Border="-"*50
    print(Border)
    print("-----Marvellous Platform Survillence System------")
    print(Border)

    # --h & --u handling
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Automation Script is used to perform")
            print("1: It fetches the information of Running Processes")
            print("2: It Fetch information about the Primary Storage as RAM")
            print("3: It Fetch information about the Sedondary Storage as HDD")
            print("4: It Fetch information about the microprocessor Storage")
            print("5: It gets auto schedule periodically")
            print("6: It maintain all Records into log file")
            print("7: It send log file through email periodically")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the Automation Script as:")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval:Time in minutes for periodic execution")
            print("Folder_Name: Name of folder for the log file creation")

        else:
            print("Unable to processed as arguments are not matching")
            print("Please use --h or --u flag for getting more details")


    elif(len(sys.argv)==3):
        PlatformSurvillance(sys.argv[2])
    else:
        print("Invalid Number of Arguments")
        print("Unable to processed as arguments are not matching")
        print("Please use --h or --u flag for getting more details")

    Border="-"*50
    print(Border)
    print("Thank you for using our automation system")
    print(Border)

if __name__=="__main__":
    main()