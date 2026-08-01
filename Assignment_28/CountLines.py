# Write a program which accepts a file name from the user and
# counts how many lines are present in the file.

import os
import sys

def CountLines(fname):

    cnt = 0
    ret = os.path.exists(fname)
    if(ret == False):
        print("File doesn't exists")
        return
    
    fobj = open(fname,"r")

    
    # for line in fobj:                   #Python internally reads the file line by line. Here line is just a variable chosen by proggrammer
    #     cnt += 1
    
    while(True):
        data = fobj.readline()
        if(data == ""):
            break
        cnt += 1

    fobj.close()
    return cnt


def main():
    Ret = CountLines(sys.argv[1])
    print(f"No of lines are : {Ret}")

if __name__ == "__main__":
    main()
