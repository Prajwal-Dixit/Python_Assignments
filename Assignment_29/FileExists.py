# Write a program which accepts a file name from the user and checks whether that file exists in the current
# directory or not.

import sys
import os

def isFileExists(fname):
    result = os.path.exists(fname)
    return result

def main():
    ret = False
    if(len(sys.argv) == 2):
        ret = isFileExists(sys.argv[1])
    else:
        print("Invalid number of arguents, please enter filename")
        sys.exit()

    if(ret == True):
        print("File Exists")
    else:
        print("File does not exists")

if __name__ == "__main__":
    main()