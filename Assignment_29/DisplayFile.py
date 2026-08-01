# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the
# console.

import sys
import os

def DisplayFile(fname):
    if(os.path.exists(fname)):
        fobj = open(fname, "r")
        contents = fobj.read()
        print(contents)
        fobj.close()

def main():
    if(len(sys.argv) == 2):
        DisplayFile(sys.argv[1])
    else:
        print("Invalid number of arguents, please enter filename")
        sys.exit()

if __name__ == "__main__":
    main()