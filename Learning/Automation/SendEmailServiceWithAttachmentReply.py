#-----------------------------------------------
# Program : Simple Gmail Mail Sneder
# Author  : Gaurav Nalawade
# Purpose : Reply to Specific Gmail email using IMAP+SMTP
#-----------------------------------------------


#-----------------------------------------------
# Required Modules
#-----------------------------------------------
import imaplib
import email
import smtplib
import mimetypes

from email.message import EmailMessage
from email.header import decode_header

#-----------------------------------------------
# Function     : send_email
# Description  : send email using Gmail SMTP server
#-----------------------------------------------
def send_email(sender,app_password,receiver,subject,body,attachment_path):

    #Step 1: Create Email Object
    msg=EmailMessage()

    #Step 2: Set mail headers
    msg["From"]=sender   
    msg["To"]=receiver
    msg["Subject"]=subject

    #Step 3: Add mail body
    msg.set_content(body)

    #Step 4:Read Attchment
    fobj=open(attachment_path,"rb")
    FileData=fobj.read()
    fobj.close()

    #Step 5:Find Attchment Type
    FileType,Encoding=mimetypes.guess_type(attachment_path)

    if FileType is None:
        MainType="application"
        SubType="octet-stream"
    else:
        MainType,SubType=FileType.split("/",1)

    #Step 6:Add Attachment
    msg.add_attachment(FileData,maintype=MainType,subtype=SubType,filename=attachment_path.split("/")[-1]) 


    #Step 7: Create SMTP SSL connection manually 
    smtp=smtplib.SMTP_SSL("smtp.gmail.com",465)

    
    #Step 8:Login using Gmail+App password
    smtp.login(sender,app_password)

    #Step 9:Send the email
    smtp.send_message(msg)

    #Step 10:Close connection manually
    smtp.quit()

#-----------------------------------------------
# Function     : main
# Description  : Driver Code
#-----------------------------------------------
def main():

    sender_email="pythont595@gmail.com"
    app_password="brik jljb ttxp fbce"

    receiver_email="gauravnalawadepatil@gmail.com"

    subject="Test Mail from Python Script"

    body="""Jay Ganesh,
    This is a test email sent using Marvellous Python.
    this email is for the testing purpose
    

    Regards,
    Gaurav Nalawade
    """

    attachment_Path="MyProfile.png"

    send_email(sender_email,app_password,receiver_email,subject,body,attachment_Path)

    print("Mail Sent Successfully")
    
#-----------------------------------------------
# Program Entry Point
#-----------------------------------------------

if __name__=="__main__":
    main()