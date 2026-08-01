# Write a program which accepts a file name and a word from the user and
# checks whether that word is present in the file or not.

import os
import sys

def CheckWord(fname, word):

    result = False
    ret = os.path.exists(fname)
    if(ret == False):
        print("File doesn't exists")
        return
    
    fobj = open(fname,"r")
    data = fobj.read()

    data = data.split()
    for ch in data:
        if(ch == word):
            result = True

    fobj.close()
    return result

def main():
    Ret = CheckWord(sys.argv[1], sys.argv[2])
    if(Ret == True):
        print(f"The word '{sys.argv[2]}' exists in file '{sys.argv[1]}' ")
    else:
        print(f"The word '{sys.argv[2]}' does not exists in file '{sys.argv[1]}' ")

if __name__ == "__main__":
    main()
