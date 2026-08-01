# 3: Write a program that schedules a function to print:
# Coding Kar..!
# every 30 minutes.

import schedule
import time

def Display(message):
    print(message)

def main():

    schedule.every(30).minutes.do(Display, "Coding Kar ...")

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()