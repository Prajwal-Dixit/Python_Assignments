# 5: Schedule a task that executes every five minutes.
# The task should write the current date and time into a file named:
# Marvellous.txt
# New entries should be appended without removing previous entries.

import schedule
import time
import datetime

def TimeLogs():
    fobj = open("Marvellous.txt", "a")
    fobj.write(f"Task executed at : {datetime.datetime.now()} \n")

def main():

    schedule.every(5).minutes.do(TimeLogs)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()