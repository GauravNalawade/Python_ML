import schedule
import time

def Codingkar():
    print("Coding kar.....!")

def main():
    schedule.every(30).minutes.do(Codingkar)


    while(True):
        schedule.run_pending()
        time.sleep(1) 
  
if __name__=="__main__":
    main()
    