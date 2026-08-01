import schedule
import time
import sys
import os

def create_logfile(file_name):
    timestamp = time.strftime("%Y_%m_%d_%H_%M_%S")
    file_name = file_name + "_" + timestamp + ".log"
    fobj = open(file_name, "w")

    fobj.write("Log file created successfully\n")
    fobj.write("Creation time : " + timestamp)

def main():
    file_name = sys.argv[1]

    schedule.every(10).minutes.do(create_logfile, file_name)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt as ke:
        print("Program execution terminated")        

if __name__ == "__main__":
    main()