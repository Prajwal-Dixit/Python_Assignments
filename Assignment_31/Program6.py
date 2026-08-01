import schedule
import time
import sys
import os

def schedule_msg(msg):
    print(msg)
    
def main():

    schedule.every().monday.at("09:00").do(schedule_msg, "Start your weekly goals")
    schedule.every().wednesday.at("17:00").do(schedule_msg, "Review your weekly progress")
    schedule.every().friday.at("18:00").do(schedule_msg, "Weekly work completed")

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt as ke:
        print("Program execution terminated")        

if __name__ == "__main__":
    main()