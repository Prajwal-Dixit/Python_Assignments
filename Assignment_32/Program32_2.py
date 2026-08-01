#Write a Python program that monitors the size of a specified file every 30 seconds.

import schedule
import time
import os
import sys

def file_size_logs(file_name):

    if not os.path.exists(file_name):
        print("File doesn't exists")
        sys.exit()
    
    border = "-"*120
    timestamp = time.strftime("%Y_%m_%d_%H_%M_%S")
    fname = "File_Logs.txt"
    
    with open(fname, "a") as fobj:
        fobj.write(border + "\n")
        fobj.write(f"File name : {file_name}\n")
        fobj.write(f"File size : {os.path.getsize(file_name)} Bytes\n")
        fobj.write(f"Creation Date and time : {timestamp} \n")
        fobj.write(border + "\n\n")

        print(f"File data is saved to {os.path.abspath(fname)}")
  
def main():
    if(len(sys.argv) != 2):
        print("Invalid number of argumments, please enter a file name")
        sys.exit()

    file = sys.argv[1]
    file = os.path.abspath(file)

    schedule.every(30).seconds.do(file_size_logs, file)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt as ke:
        print("Program execution terminated")        

if __name__ == "__main__":
    main()