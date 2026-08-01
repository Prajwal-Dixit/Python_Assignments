#Copy File Contents into Another File

import os
import sys

def CopyFiles(fname1, fname2):

    if(os.path.exists(fname1) == False):
        print("Source file does'nt exists")
        return 
    
    fobj1 = open(fname1, "r")
    fobj2 = open(fname2, "w")

    data = fobj1.read()
    fobj2.write(data)
    print(f"Contents of file {fname1} are copied in {fname2}")

    fobj1.close()
    fobj2.close()

def main():

    if(len(sys.argv) != 3):
        print("Invalid number of argumments")
        sys.exit()
    
    CopyFiles(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
