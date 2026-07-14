#Write a program that calculates 1^5+2^5+3^5+.....+N^5
#for multiple values of N simultaneously using Pool.
#list.

import multiprocessing
import time

def SumPower(no):
    sum = 0
    for i in range(1, no+1):
        sum = sum + (i **5)
    return sum

def main():
    print(SumPower(15))
    Start_time = time.perf_counter()
    Data = list()
    print("Enter no of elements")
    No = int(input())
    print("Enter elements one by one")

    for i in range(0,No):
        Data.append(int(input()))

    p = multiprocessing.Pool()
    result = p.map(SumPower, Data)

    print(result)
    p.close()
    p.join()

    Stop_time = time.perf_counter()

    print(f"Execution time : {Stop_time - Start_time}")
if __name__ == "__main__":
    main()