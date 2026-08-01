#######################################################################################################
#   Function name :         CalulateChecksum
#   Input :                 Name of file
#   Description :           Calculates checksum of a file
#   Date :                  26/07/2026
#   Author :                Prajwal
########################################################################################################

import os
import hashlib

def CalculateCheckSum(FileName):

    if not (os.path.exists(FileName)):
        print(f"File {FileName} does not exists")
        return
    if not (os.access(FileName, os.R_OK)):
        print(f"File {FileName} is not readable")
        return
    if not (os.path.isfile(FileName)):
        print(f"{FileName} is not a regular file")
        return 
    if not (os.access(FileName, os.W_OK)):
        print(f"File {FileName} cannot be deleted")
        return
    
    fobj = open(FileName, "rb")             
    
    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()                            
    return hobj.hexdigest()               