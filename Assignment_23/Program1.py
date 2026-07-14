#Write a program that calculates 1^5+2^5+3^5+.....+N^5
#for multiple values of N simultaneously using Pool.

#IMP program for list ::>>

import multiprocessing
import os

def SumEven(no):
    sum = 0
    for i in range(1, no+1):
        if(i % 2 == 0):
            sum = sum + i
    return (os.getpid(),sum,no)         #Returning in the form of tuple

######################################----OR----########################################
"""
    for i in range(2, no+1,2):
        sum = sum + i
    return sum
"""
#########################################################################################

def main():
    Data = list()
    process = []
    print("Enter no of elements")
    No = int(input())
    print("Enter elements one by one")

    for i in range(0,No):
        Data.append(int(input()))

    p = multiprocessing.Pool()
    result = p.map(SumEven, Data)   #This creates a list of tuples, not just integers
    #This list will look like : [(1012, 192929, 10), (1221, 223221, 20), (2122, 134423, 30)]
    #We can unpack them like : for no1, no2, no3 in result :

    for pid, sum, no in result:
        print(f"Process Id : {pid}, Input number: {no}, Sum of even nummbers : {sum}")

    p.close()
    p.join()

if __name__ == "__main__":
    main()
