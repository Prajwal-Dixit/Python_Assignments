#######################################################################################################
#
#   Importing required libraries
#
########################################################################################################

import sys 
import schedule        
import time
from SendMail import send_mail
from Checksum import CalculateCheckSum
from DeleteDuplicate import DeleteDuplicate

#######################################################################################################
#   Function name :         main
#   Input :                 Command line argumments
#   Description :           It controls the script
#   Date :                  26/07/2026
#   Author :                Prajwal
########################################################################################################

def main():
    border = "-"*80
    print(border)
    print("Duplicate remover automation script")
    print(border)

    if(len(sys.argv) == 4):
        if not (sys.argv[2].isdigit()):
            print("Given interval is not a numeric value")
            sys.exit()

        interval = int(sys.argv[2])

        if (interval <= 0):
            print("Invalid time interval")
            sys.exit()
        
        schedule.every(interval).minutes.do(DeleteDuplicate, sys.argv[1], sys.argv[3])
        while(True):
            schedule.run_pending()
            time.sleep(1)

    elif(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script deletes duplicate files from the directory")
            print("For better usage, print --u flag")

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as :")
            print("python3 Filename.py <DirectoryName> <TimeIntervalInMinutes> <RecieverEmailAddress")
            print("Directory name must be the absolute path")

        else:
            print("Invalid number of arguments")
            print("Please use --h or --u for more information")

    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

    print(border)
    print("Thank you for using Duplicate remover automation script")
    print(border)

if __name__ == "__main__":
    main()
