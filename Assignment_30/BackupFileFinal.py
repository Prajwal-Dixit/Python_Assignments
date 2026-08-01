#######################################################################################################
#
#   Importing required libraries
#
########################################################################################################

import time
import os
import sys
import schedule
import shutil

Border = "-"*100

#######################################################################################################
#   Function name :         Backup_File
#   Input :                 Name of directory and File
#   Description :           Backups the mentioned files into given directory
#   Date :                  27/07/2026
#   Author :                Prajwal
########################################################################################################

def Backup_File(DirectoryName, SourceFile):
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

    temp_file = os.path.basename(SourceFile)
    name, ext = os.path.splitext(temp_file)
    BackupFile = name + "_" + timestamp + ext
    BackupFile = os.path.join(DirectoryName, BackupFile)

    Logfile = "backup_log.txt"
    fobj = open(Logfile, "a")

    try:
        shutil.copy2(SourceFile, BackupFile)
    except Exception as e:
        print(f"Backup failed : {e}")

    fobj.write(f"File with name {SourceFile} is backed up in the {DirectoryName} directory at {timestamp}\n")
    fobj.write(Border + "\n")

    print(f"File with name {SourceFile} is backed up in the {DirectoryName} directory at {timestamp}")
    print(Border + "\n")

    fobj.close()

#######################################################################################################
#   Function name :         main
#   Input :                 Command line argumments
#   Description :           It controls the script
#   Date :                  27/07/2026
#   Author :                Prajwal
########################################################################################################

def main():
    
    print(Border)
    print("File Backup Automation script")
    print(Border)

    if(len(sys.argv) == 3):
        schedule.every(0.3).minutes.do(Backup_File, sys.argv[1], sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)

    elif(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used backup the file in a folder")
            print("For better usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as : ")
            print("python FileName.py DirectoryName FileName")

        else:
            print("Invalid number of arguments")
            print("Please use --h or --u for more information")

    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

    print(Border)
    print("Thank you for using File Backup Automation script")
    print(Border)
    

if __name__ == "__main__":
    main()