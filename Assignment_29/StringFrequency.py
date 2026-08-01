# Write a program which accepts a file name and one string from the user and returns the frequency (count of
# occurrences) of that string in the file.

import sys
import os

def Frequency(fname, word):
    cnt = 0
    ret = os.path.exists(fname)
    if(ret == False):
        print("file does not exists, please enter valid file name")
    else:
        fobj = open(fname, "r")
        contents = fobj.read()
        contents = contents.split()

        cnt = contents.count(word)

        # for i in contents:
        #     if(i == word):
        #         cnt += 1

        fobj.close()
        return cnt

def main():
    ret = 0
    if(len(sys.argv) == 3):
        ret = Frequency(sys.argv[1], sys.argv[2])
        print(f"Number of occurence of string {sys.argv[2]} is {ret}")
    else:
        print("Invalid number of arguents, please enter a filename and a string")

if __name__ == "__main__":
    main()