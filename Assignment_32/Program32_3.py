# Write a program that reads and displays the contents of a specified
# text file every minute.

import schedule
import time
import os
import sys

def file_display(file_name):

    if not os.path.exists(file_name):
        print("File doesn't exists")
        sys.exit()

    elif (os.path.getsize(file_name) == 0):
        print("Given file is empty")
        sys.exit()
    try:
        fobj = open(file_name, "r")
        print(fobj.read())
        fobj.close()

    except PermissionError as pe:
        print(pe)

    except Exception as e:
        print("File can't be opened ", e)    
  
def main():
    if(len(sys.argv) != 2):
        print("Invalid number of argumments, please enter a file name")
        sys.exit()

    file = sys.argv[1]
    file = os.path.abspath(file)

    schedule.every(1).minute.do(file_display, file)

    while (True):
        schedule.run_pending()
        time.sleep(1)
      

if __name__ == "__main__":
    main()