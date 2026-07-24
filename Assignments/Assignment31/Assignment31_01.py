import schedule
import time
from num2words import num2words

def Display(Msg,Interval):
    print(Msg)
    print(f"Every {num2words(Interval)} Seconds")

def main():
    print("Enter Message:")
    message=input()

    print("Enter interval in seconds:")
    interval=int(input())

    if(interval>0):
        schedule.every(interval).seconds.do(Display,message,interval)
    else:
        print("Interval should be Greater than 0 Seconds")
        return
    
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()

