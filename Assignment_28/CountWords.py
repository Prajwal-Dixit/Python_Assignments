# Write a program which accepts a file name from the user 
# and counts the total number of words in that file.

import os
import sys

def CountWords(fname):

    cnt = 0
    ret = os.path.exists(fname)
    if(ret == False):
        print("File doesn't exists")
        return
    
    fobj = open(fname,"r")
    data = fobj.read()

    data = data.split()
    for no in data:
        cnt += 1

    fobj.close()
    return cnt


def main():
    Ret = CountWords(sys.argv[1])
    print(f"No of words are : {Ret}")

if __name__ == "__main__":
    main()
