# Write a program that scans a specified directory every minute.
# The task should display:
# • Directory name
# • Number of files
# • Number of subdirectories
# • Date and time of scanning

import schedule
import time
import sys
import os

def scan_directory(directory_name):
    total_files = 0
    total_subfolders = 0
    timestamp = time.strftime("%Y_%m_%d : %H_%M_%S")

    for folder_name, sub_folder, file_name in os.walk(directory_name):
        for subf in sub_folder:
            total_subfolders += 1

            for fname in file_name:
                total_files = total_files + 1

    print(f"Directory name : {directory_name}")
    print(f"Total number of files are : {total_files}")
    print(f"Total number of sub directories are : {total_subfolders}")
    print(f"Date and time of scanning : {timestamp}")

def main():
    directory = sys.argv[1]

    schedule.every(1).minute.do(scan_directory, directory)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt as ke:
        print("Program execution terminated")        

if __name__ == "__main__":
    main()