import sys
import os
import hashlib
import schedule
import time
import datetime
import smtplib
from email.message import EmailMessage 
import mimetypes

def send_email(sender_email,app_password,subject,body,attachment,receiver_email):
    msg=EmailMessage()  
     
    msg["From"]=sender_email
    msg["To"]=receiver_email 
    msg["Subject"]=subject  

    msg.set_content(body)

    fobj=open(attachment,"rb")
    FileData=fobj.read()
    fobj.close()

    FileType,Encoding=mimetypes.guess_type(attachment)

    if FileType is None:
        MainType="application" 
        SubType="octet-stream" 
    else:
        MainType,SubType=FileType.split("/",1)

    msg.add_attachment(
                        FileData,
                        maintype=MainType,
                        subtype=SubType,
                        filename=os.path.basename(attachment)
                        
                      )


    try:

        smtp=smtplib.SMTP_SSL("smtp.gmail.com",465)

        smtp.login(sender_email,app_password)

        smtp.send_message(msg)
    
        smtp.quit()

        return True

    except Exception as e:
        print("Unable to send email")
        print("Error:",e)
        return False


def CalculateChecksum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if Ret == False:
        print("Path is invalid")
        return

    Ret = os.path.isdir(DirectoryName)

    if Ret == False:
        print("It is not a directory")
        return

    Duplicate = {}
    
    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)

            Checksum = CalculateChecksum(fname)

            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]

    return Duplicate

def DeleteDuplicate(DirectoryName,LogFolderName,Receiver_email):
    Border="-"*50 

    Ret=False
    Ret=os.path.exists(LogFolderName)

    if(Ret==True):
        Ret=os.path.isdir(LogFolderName)
        if(Ret==False):
            print("Unable to procces aas directory name is existing but its not a directory")
            return
    else:
        os.mkdir(LogFolderName) 
        print("Directory for the log file gets created successfully")

    timestamp=time.strftime("%d_%m_%Y_%I_%M_%S")

    FileName=os.path.join(LogFolderName,"DuplicateRemovalLog_%s.txt" %timestamp)

    fobj=open(FileName,"w")

    print(f"Log file gets successfully created with name {FileName}\n")

    fobj.write(Border+"\n")
    fobj.write("---------Duplicate File Removal Automation--------\n")
    fobj.write("Log file gets created at :"+timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write(Border+"\n")
    fobj.write("---------------Deleted Files Report---------------\n")
    fobj.write(Border+"\n\n")


    StartTime=datetime.datetime.now()

    fobj.write(
              f"Starting time of directory scanning :"
              f"{StartTime.strftime('%d_%m_%Y %H:%M:%S %p')}\n"
              )

    MyDict = FindDuplicate(DirectoryName) 

    EndTime=datetime.datetime.now()

    fobj.write(
              f"Completion time of directory scanning :"
              f"{EndTime.strftime('%d_%m_%Y %H:%M:%S %p')}\n")

    fobj.write(f"Scanned directory name: {DirectoryName}\n")

    TotalFilesScanned=0
    for value in MyDict.values():
        TotalFilesScanned +=len(value)
    fobj.write(f"Total number of files scanned: {TotalFilesScanned}\n")
    
    Result = list(filter(lambda x : len(x) > 1, MyDict.values())) 
     
    TotalFiles=0 
    Count = 0 
    TotalDeleted = 0
    DeletedFilepaths=[]

    for value in Result:
        TotalFiles += len(value) 
        Count=0 
        for subvalue in value:
            Count = Count + 1 
            if(Count > 1):
                try:
                    os.remove(subvalue)
                    DeletedFilepaths.append(subvalue)
                    TotalDeleted = TotalDeleted + 1
                except PermissionError as e:
                    print("Unable To Remove file:",e)

    fobj.write(f"Total number of Duplicate files found: {TotalFiles}\n")
    fobj.write(f"Total number of duplicate files deleted : {TotalDeleted}\n")

    for CheckSum,files in MyDict.items():
        if len(files)>1:
            fobj.write(Border+"\n")
            fobj.write(f"Checsum: {CheckSum}\n")
            for file in files:
                fobj.write(f"File : {file}\n")
            fobj.write(Border+"\n\n")

    fobj.write("Complete paths of all deleted duplicate files:\n")
    for path in DeletedFilepaths:
        fobj.write(f"path:{path}\n")

    fobj.close()

    Sender_email="pythont595@gmail.com"
    App_password="jali gakc lhlx gmtl"


    Subject="Duplicate file removal report"

    body=f"""Jay Ganesh,

        The duplicate-file removal operation has been completed successfully.

        Operation Statistics:

        Starting time of scanning:{StartTime.strftime('%d_%m_%Y %H:%M:%S %p')}

        Completion time of directory scanning :{EndTime.strftime('%d_%m_%Y %H:%M:%S %p')}

        Directory scanned: {DirectoryName}

        Total number of files scanned:{TotalFilesScanned}

        Total number of duplicate file found:{TotalFiles}

        Total number of duplicate files deleted:{TotalDeleted}

        
        Please find the detailed log file attached to this email.

        Thanks Regards,
        Gaurav Nalawade
     """
    Attachment=FileName
    
    Ret=send_email(Sender_email,App_password,Subject,body,Attachment,Receiver_email)
    fobj=open(FileName,"a")
    if(Ret==True):
        fobj.write("Mail Sent Sucessfully")
    else:  
        fobj.write("Mail Sent Failed!!!!!!")
    fobj.close()

    
def main():

    if (len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This automation script is used to Delete Duplicate Files")
            print("1 : This script scans a directory,identifies duplicate files using cehcksums")
            print("2 : delete Duplicate Files")
            print("3 : It gets auto scheduled periodically")
            print("4 : It Create a log File & maintains all records into log file")
            print("5 : It sends the log files through mail periodically")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the automation script as")
            print(f"python <{sys.argv[0]}> <Time_Interval> <Directory_Path> <LogDirectory_Name> <Reciver_email>")
            print("Time_Interval  : Time in minutes for periodic execution")
            print("Directory_path : FolderName that you want to Scanned")
            print("LogDirectory_Name : Name of folder for the log file creation")
            print("Reciver_email :  Receiver email that accpets log file")
        else:
            print("Unable to proceed as there is no matching arguments")
            print("Please use --h or --u for getting more details") 
    elif(len(sys.argv)==5):
        if(int(sys.argv[1])>0):
            schedule.every(int(sys.argv[1])).minutes.do(DeleteDuplicate,sys.argv[2],sys.argv[3],sys.argv[4])

            while(True):
                schedule.run_pending() 
                time.sleep(1)
        else:
            print("Time Interval should be Greater than 0")
    else:
        print("Unable to proceed as there is no mathching arguments")
        print("Please use --h or --u for gettinng more details")

if __name__ == "__main__": 
    main()