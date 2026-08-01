# Write a Python program that prints:
# Jay Ganesh...
# every two seconds.

import schedule
import time

def Display(message):
    print(message)

def main():

    schedule.every(2).seconds.do(Display, "Jay Ganesh ...")

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
