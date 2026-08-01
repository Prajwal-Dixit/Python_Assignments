# Write a program that deletes all empty files from a specified
# directory every hour.

import schedule
import time
import os
import sys

border = "-"*120

def delete_emptys(directory_name):
    if not os.path.exists(directory_name):
        print("Source directory doesn't exists")
        return

    if not os.path.isdir(directory_name):
        print(f"{directory_name} is not a directory")
        return
    
    timestamp = time.strftime("%Y_%m_%d : %H_%M_%S")

    LogFile = "Empty_files_logs.txt"
    fobj = open(LogFile, "a")

    fobj.write(border + "\n")
    fobj.write("Deleted empty files are : \n")
    fobj.write(border + "\n")

    count = 0
    for FolderName, SubFolder, FileName in os.walk(directory_name):
        for fname in FileName:
            file_path = os.path.join(FolderName, fname)
            if(os.path.getsize(file_path) == 0):                
            
                try :
                    os.remove(file_path)
                    count = count + 1
                    fobj.write(file_path + "\n")
                except OSError as e:
                    print(f"Could not delete {fname} due to {e}")

    fobj.write(border + "\n")
    fobj.write(f"Empty files deleted on : {timestamp} \n")
    fobj.write(border + "\n")
    fobj.write(f"Nummber of empty files deleted are : {count} \n")
    fobj.write(border + "\n\n\n")

    fobj.close()

    print(f"Deleted Empty files are listed in the {os.path.abspath(LogFile)}  at {timestamp}")
  
def main():
    print(border)
    print("---------Empty files remover---------")
    print(border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to delete all the empty files of a directory")
            print("For better usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as : ")
            print("python FileName.py directory_name")

        else:
            schedule.every(1).hour.do(delete_emptys, sys.argv[1])
            while (True):
                schedule.run_pending()
                time.sleep(1)

    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

    print(border)
    print("----------Thank you for using Empty file remover-----------")
    print(border)

if __name__ == "__main__":
    main()