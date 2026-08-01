# Write a program which accepts a file name from the user and
# displays the contents of the file line by line on the screen.

import os
import sys

def DisplayLines(fname):

    cnt = 0
    ret = os.path.exists(fname)
    if(ret == False):
        print("File doesn't exists")
        return
    
    fobj = open(fname,"r")

    for line in fobj:              
        print(line, end = "")
    print()

    fobj.close()


def main():
    DisplayLines(sys.argv[1])

if __name__ == "__main__":
    main()
