import schedule
import time

def MondayTask():
    print("Monday at 9:00 AM: Start your work goals")

def wednesday():
    print("Wednesday at 5:00 PM: Review your weekly progress")

def friday():
    print("Friday at 6:00 PM: Weekly work completed")

def main():
    schedule.every().monday.at("09:00").do(MondayTask) 
    schedule.every().wednesday.at("17:00").do(wednesday) 
    schedule.every().friday.at("18:00").do(friday)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()