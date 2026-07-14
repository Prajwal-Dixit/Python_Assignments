"""
For every number in the given list, count how many prime numbers
exist between 1 and N using multiprocessing Pool.
"""

import os
import multiprocessing

def CountPrime(no):
    cnt = 0
    for i in range(1, no):
        check = False
        if(i == 2):
            cnt = cnt + 1
            continue
        elif(i == 1):
            continue

        for j in range(2, i): 
            if(i % j == 0):
                check = True
                break
        if(check == False):
            cnt = cnt + 1
    
    return cnt

def main():
    Data = list()
    print("Enter no of elements")
    No = int(input())
    print("Enter elements one by one")

    for i in range(0,No):
        Data.append(int(input()))

    p = multiprocessing.Pool()
    result = p.map(CountPrime, Data)
    

    for i in range(0, len(result)):
        print(f"Number of prime numbers in 1 to {Data[i]} is : {result[i]}")
        
    p.close()
    p.join()

if __name__ == "__main__":
    main()