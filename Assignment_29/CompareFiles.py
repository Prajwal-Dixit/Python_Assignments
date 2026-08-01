# Write a program which accepts two file names through command line arguments and compares the contents of
# both files.
# • If both files contain the same contents, display Success
# • Otherwise display Failure

import sys
import os

def CompareFiles(fname1, fname2):
    result = False
    ret1 = os.path.exists(fname1)
    ret2 = os.path.exists(fname2)

    if(ret1 == False):
        print(f"{fname1} File does not exits, enter a valid file name")
    elif(ret2 == False):
        print(f"{fname2} File does not exits, enter a valid file name")

    else:
        fobj1 = open(fname1, "r")
        contents1 = fobj1.read()

        fobj2 = open(fname2, "r")
        contents2 = fobj2.read()

        fobj1.close()
        fobj2.close()
        
        if(contents1 == contents2):
            result = True
            return result
        else:
            return result

def main():
    ret = False
    if(len(sys.argv) == 3):
        ret = CompareFiles(sys.argv[1], sys.argv[2])
    else:
        print("Invalid number of arguents, please enter two filenames")

    if(ret == True):
        print("Success")
    else:
        print("Failure")
        
if __name__ == "__main__":
    main()