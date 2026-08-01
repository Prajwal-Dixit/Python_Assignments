# 2: Write a Python program that displays the current date and time
# after every one minute.
# Use the datetime module.

import schedule
import time
import datetime

def Display():
    print(f"Current date and time : {datetime.datetime.now()}")

def main():

    schedule.every(1).minute.do(Display)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()