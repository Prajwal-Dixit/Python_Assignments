# Write a program which accepts an existing file name through command line arguments, creates a new file
# named Demo.txt, and copies all contents from the given file into Demo.txt.

import sys
import os

def CopyFile(fname):
    ret = os.path.exists(fname)
    if(ret == False):
        print("File does not exits, enter a valid file name")

    else:
        fobj1 = open(fname, "r")
        contents = fobj1.read()

        fobj2 = open("Demo.txt", "w")
        fobj2.write(contents)
        print(f"Contents of file {fname} are successfully copied in file {fobj2.name}")

        fobj1.close()
        fobj2.close()

def main():
    if(len(sys.argv) == 2):
        CopyFile(sys.argv[1])
    else:
        print("Invalid number of arguents, please enter a filename")

if __name__ == "__main__":
    main()
  
