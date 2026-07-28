#-----------------------------------------------
# Program : Simple Gmail Mail Sneder
# Author  : Gaurav Nalawade
# Purpose : Send mail using Python SMTP 
#-----------------------------------------------


#-----------------------------------------------
# Required Modules
#-----------------------------------------------
import smtplib
from email.message import EmailMessage

#-----------------------------------------------
# Function     : send_email
# Description  : send email using Gmail SMTP server
#-----------------------------------------------
def send_email(sender,app_password,receiver,subject,body):

    #Step 1: Create Email Object
    msg=EmailMessage()

    #Step 2: Set mail headers
    msg["From"]=sender
    msg["To"]=receiver
    msg["Subject"]=subject

    #Step 3: Add mail body
    msg.set_content(body)

    #Step 4: Create SMTP SSL connection manually 
    smtp=smtplib.SMTP_SSL("smtp.gmail.com",465)

    #Step 5:Login using Gmail+App password
    smtp.login(sender,app_password)

    #Step 6:Send the email
    smtp.send_message(msg)

    #Step 7:Close connection manually
    smtp.quit()

#-----------------------------------------------
# Function     : main
# Description  : Driver Code
#-----------------------------------------------
def main():

    sender_email="pythont595@gmail.com"
    app_password="brik jljb ttxp fbce"

    receiver_email="bachcheakshata@gmail.com"

    subject="Test Mail from Python Script"

    body="""Jay Ganesh,
    This is a test email sent using Marvellous Python.
    this email is for the testing purpose
    

    Regards,
    Gaurav Nalawade
    """

    send_email(sender_email,app_password,receiver_email,subject,body)

    print("Mail Sent Successfully")
    
#-----------------------------------------------
# Program Entry Point
#-----------------------------------------------

if __name__=="__main__":
    main()