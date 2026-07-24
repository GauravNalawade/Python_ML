import schedule
import time
import datetime
 
def CurrentDateTime():
    CurrentDateTime=datetime.datetime.now() 
    print("Current Date and Time : ",CurrentDateTime.strftime("%d-%m-%Y %I:%M:%S %p"))

def main():
     schedule.every(1).minutes.do(CurrentDateTime)
    
     while(True):
          schedule.run_pending()
          time.sleep(30)

if __name__=="__main__":
     main()