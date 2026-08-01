# Write a program that copies all .txt files from one directory to
# another every ten minutes.

import schedule
import time
import os
import sys
import shutil

border = "-"*120

def directory_copy(source_dir, destination_dir):
    if not os.path.exists(source_dir):
        print("Source directory doesn't exists")
        return

    if not os.path.isdir(source_dir):
        print(f"{source_dir} is not a directory")
        return

    if not os.path.exists(destination_dir):
        print("Destination directory doesn't exists")
        return

    if not os.path.isdir(destination_dir):
        print(f"{destination_dir} is not a Directory")
        return

    timestamp = time.strftime("%Y_%m_%d : %H_%M_%S")

    LogFile = "FileCopy_logs.txt"
    fobj = open(LogFile, "a")

    fobj.write(border + "\n")
    fobj.write("Copied files are : \n")
    fobj.write(border + "\n")

    count = 0
    for FolderName, SubFolder, FileName in os.walk(source_dir):
        for fname in FileName:
            name, ext = os.path.splitext(fname)
            if(ext == ".txt"):
                dest_path = os.path.join(destination_dir, fname)
                source_path = os.path.join(FolderName, fname)

                try :
                    shutil.copy2(source_path, dest_path)
                    count = count + 1
                    fobj.write(fname + "\n")
                except OSError as e:
                    print(f"Could not copy {fname} due to {e}")

    fobj.write(border + "\n")
    fobj.write(f"Files copied on : {timestamp} \n")
    fobj.write(border + "\n")
    fobj.write(f"Nummber of Files copied are : {count} \n")
    fobj.write(border + "\n\n\n")

    fobj.close()

    print(f"Files are copied in the {destination_dir} directory at {timestamp}")
  
def main():
    print(border)
    print("Directory File Backup Automation script")
    print(border)

    if(len(sys.argv) == 3):
            schedule.every(10).minutes.do(directory_copy, sys.argv[1], sys.argv[2])

            while (True):
                schedule.run_pending()
                time.sleep(1)
      

    elif(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used backup all the files of a directory in another directory")
            print("For better usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as : ")
            print("python FileName.py source_directory destination_directory")

        else:
            print("Invalid number of arguments")
            print("Please use --h or --u for more information")

    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

    print(border)
    print("Thank you for using File Backup Automation script")
    print(border)

if __name__ == "__main__":
    main()