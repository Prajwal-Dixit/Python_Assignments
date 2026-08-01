import schedule
import time
import sys
import os

def scan_directory(directory_name):

    border = "-"*120
    if not (os.path.exists(directory_name)):
        print("Directory doesn't exists")
        return
    if not (os.path.isdir(directory_name)):
        print("Given input is not a directory")
        return 
    
    total_files = 0
    timestamp = time.strftime("%Y_%m_%d : %H_%M_%S")

    for folder_name, sub_folder, file_name in os.walk(directory_name):
        for fname in file_name:
            total_files = total_files + 1

    with open("DirectoryCountLog.txt", "a") as fobj:
        fobj.write(f"Directory name : {directory_name}\n")
        fobj.write(f"Total number of files are : {total_files}\n")
        fobj.write(f"Date and time of scanning : {timestamp}\n\n")
        fobj.write(border + "\n")   

def main():
    directory = sys.argv[1]

    if not (os.path.isabs(directory)):
        print("Enter absolute path os the directory")
        sys.exit()

    schedule.every(5).minutes.do(scan_directory, directory)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt as ke:
        print("Program execution terminated")        

if __name__ == "__main__":
    main()