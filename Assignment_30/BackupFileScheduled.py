# Write a Python program that performs a file backup every hour.
# The program should:
#
# 1. Accept the source file path.
# 2. Accept the destination directory path.
# 3. Copy the source file to the destination directory.
# 4. Add the current date and time to the backup filename.
# 5. Write the backup operation details into:
#    backup_log.txt

import time
import os
import sys
import schedule

Border = "-"*100

def Backup(DirectoryName, SourceFile):

    ret = os.path.exists(DirectoryName)
    if(ret == False):
        print("The given directory name does not exists")
        return
    
    ret = os.path.isdir(DirectoryName)
    if(ret == False):
        print("The given File is not a directory")    
        return
            
    ret = os.path.exists(SourceFile)
    if(ret == False):
        print("The sourcefile does not exists, please enter a valid source file name")
        return


    timestamp = time.strftime("%Y_%m_%d_%H_%M_%S")

    name, ext = os.path.splitext(SourceFile)
    BackupFile = name + "_" + timestamp + ext
    BackupFile = os.path.join(DirectoryName, BackupFile)

    Logfile = "backup_log.txt"
    fobj3 = open(Logfile, "a")

    fobj1 = open(SourceFile, "r")
    fobj2 = open(BackupFile, "w")

    fobj2.write(fobj1.read())
    fobj3.write(f"File with name {SourceFile} is backed up in the {DirectoryName} directory at {timestamp}\n")
    fobj3.write(Border + "\n")

    print(f"File with name {SourceFile} is backed up in the {DirectoryName} directory at {timestamp}")
    print(Border + "\n")
    
def main():
    
    print(Border)
    print("File Backup Automation script")
    print(Border)

    if(len(sys.argv) == 3):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used backup the file in a folder")
            print("For better usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as : ")
            print("python FileName.py DirectoryName FileName")

        else:
            schedule.every(1).minute.do(Backup, sys.argv[1], sys.argv[2])

            while(True):
               schedule.run_pending()
               time.sleep(1)

    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

    print(Border)
    print("Thank you for using File Backup Automation script")
    print(Border)
    

if __name__ == "__main__":
    main()