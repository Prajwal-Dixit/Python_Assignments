#######################################################################################################
#   Function name :         FindDuplicate
#   Input :                 Name of directory
#   Description :           Identifies all duplicate files 
#   Date :                  26/07/2026
#   Author :                Prajwal
########################################################################################################

import os
from Checksum import CalculateCheckSum
import re

def FindDuplicate(DirectoryName, email_address):
    Ret = False

    Ret = os.path.exists(DirectoryName)             #Filter 1
    if(Ret == False):
        print("Path is invalid")
        return

    Ret = os.path.isdir(DirectoryName)              #Filter 2
    if(Ret == False):
        print("It is not a directory")
        return

    Ret = os.path.isabs(DirectoryName)              #Filter 3
    if(Ret == False):
        print("Please enter absolute path of the directory")
        return

    Ret = os.access(DirectoryName, os.R_OK)
    if(Ret == False):
        print("Directory does not have read permission")
        return
    
    Ret = os.access(DirectoryName, os.W_OK)
    if(Ret == False):
        print("Directory does not have write permission")
        return

    Ret = os.access(DirectoryName, os.X_OK)
    if(Ret == False):
        print("Directory does not have traversal permission")
        return

    pattern = r'^[A-Za-z0-9._%+-]+@gmail\.com$'
    Ret = re.fullmatch(pattern, email_address)
    if(Ret == False):
        print("Invalid email address, enter in the format @gmail.com")
        return
    
    Duplicate = {}                                  #Syntax to create empty set or dictionary
    total_files = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):

        for fname in FileName:
            total_files += 1

            fname = os.path.join(FolderName, fname)

            CheckSum = CalculateCheckSum(fname)

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fname)           #File already exists, so append file name to the same key
            else:
                Duplicate[CheckSum] = [fname]

    return Duplicate, total_files
