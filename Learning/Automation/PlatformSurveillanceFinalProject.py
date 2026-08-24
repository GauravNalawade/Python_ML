import psutil
import sys
import os
import time
import schedule 
import smtplib
import mimetypes
from email.message import EmailMessage

def sendEmail(sender_mail,app_password,receiver_mail,subject,body,attachment_path):

    msg=EmailMessage()
    
    msg["From"]=sender_mail
    msg["To"]=receiver_mail
    msg["Subject"]=subject

    msg.set_content(body)

    fobj=open(attachment_path,"rb")
    FileData=fobj.read()
    fobj.close()

    FileType, Encoding = mimetypes.guess_type(attachment_path)

    if FileType is None:
        MainType="application"
        SubType="octet-stream"
    else:
        MainType,SubType=FileType.split("/",1)

    msg.add_attachment(FileData,
                        maintype=MainType, 
                        subtype=SubType,
                        filename=attachment_path.split("/")[-1])
    try:

        smtp=smtplib.SMTP_SSL("smtp.gmail.com",465)

        smtp.login(sender_mail,app_password)

        smtp.send_message(msg)
    
        smtp.quit()
    except Exception as e:
        print("Unable to send email")
        print("Error:", e)


def ProcessScan():
    listprocess = []

    for proc in psutil.process_iter():   
        info = proc.as_dict(attrs=["pid","name","username","status","cmdline"])
        info["cpu_percent"] = proc.cpu_percent(None)
        info["memory_percent"] = proc.memory_percent()

        listprocess.append(info)

    return listprocess
    
def PlatformSurvillance(FolderName): 
    Border = "-"*50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to proceed as directory name is existing but its not a adirectory")
            return
    else:   
        os.mkdir(FolderName)
        print("Directory for the logfile gets created succesfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Data_%s.txt" %timestamp)

    fobj = open(FileName,"w")

    print(f"Log file gets succesfully created with name {FileName}")

    fobj.write(Border+"\n")
    fobj.write("----Platform Surveillance  System ----\n")
    fobj.write("Log file gets created at : "+timestamp+"\n") 
    fobj.write(Border+"\n\n")

    fobj.write("---------------- System Report -----------------\n")

    # CPU information
    fobj.write("Number of active CPU cores : %s\n" %psutil.cpu_count())
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    # RAM information
    memory = psutil.virtual_memory()  

    fobj.write("RAM Usage : %s %%\n" %memory.percent) 
    TotalRAMGB = memory.total / (1024 * 1024 * 1024)
    fobj.write(f"Total RAM : {TotalRAMGB:.2f} GB\n")
        
    fobj.write(Border+"\n")

    # Netork Usage
    netobj = psutil.net_io_counters() 

    fobj.write("Network Usage Report\n")
    fobj.write("Sent : %.2f MB\n" %(netobj.bytes_sent / (1024 * 1024)))
    fobj.write("Receive : %.2f MB\n" %(netobj.bytes_recv / (1024 * 1024)))
    
    # Process log
    Data = ProcessScan()
 
    for info in Data:
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("User Name : %s\n" %info.get("username")) 
        fobj.write("Status : %s\n" %info.get("status"))
        fobj.write("CPU usage : %.2f\n" %info.get("cpu_percent"))
        fobj.write("RAM usage : %.2f\n" %info.get("memory_percent"))

        # fobj.write("Command : %s\n" %info.get("cmdline"))

        Command = info.get("cmdline")
        if Command:
            fobj.write("Command : %s\n" % " ".join(Command))
        else:
            fobj.write("Command : Not Available\n")

        fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("--------------- End of Log File ----------------\n")
    fobj.write(Border+"\n")

    fobj.close()
   
    Sender_Email="----------------@gmail.com"
    App_password="---- ---- ---- ----"
    Receiver_mail="---------------@gmail.com"
    Subject="Platform Surveillance System Summary Report"
    Body=""" Hello this email contains the Platform Surveillance System Summary Report

    This is auto generated mail pls do not reply

    Thanks Regards,
    Gaurav Nalawade
    """
    Attachment=FileName

    sendEmail(Sender_Email,App_password,Receiver_mail,Subject,Body,Attachment)
    print("Mail sent Successfully")

def main():
    Border = "-"*50
    print(Border)
    print("---- Platform Surveillance  System ----")
    print(Border)

    # --h & --u handling
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to perform ")
            print("1 : It fetch the information of running processess")
            print("2 : It fetch information about the primary storage as RAM")
            print("3 : It fetch information about the secondary storage as HDD")
            print("4 : It fetch the information about the microprocessor")
            print("5 : It gets auto scheduled periodically")
            print("6 : It maintains all records into log file")
            print("7 : It sends the log files through mail periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as : ")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name : Name of folder for the log file creation")
            
        else:
            print("Unable to proceed as there is no matching argument")
            print("Please use --h or --u flag for getting more details")

    # Actual project code
    elif(len(sys.argv) == 3):

        #print("CPU Usage : ",psutil.cpu_percent())

        print("Schedular started succesfully")
        print("Press Ctrl + C to abort the automation script")
        
        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillance, sys.argv[2],)
        
        while True:
            schedule.run_pending()
            time.sleep(1)

    else: 
        print("Invalid number of argumenst")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for getting more details")

    print(Border)
    print("--- Thank you for using our automation System ---")
    print(Border)

if __name__ == "__main__":
    main() 