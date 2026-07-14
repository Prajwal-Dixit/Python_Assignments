"""
Write a program that calculates factorials of multiple numbers
simultaneously using Pool.map().
"""
import os
import multiprocessing

def Factorial(no):
    fact = 1
    ProcessID = os.getpid()
    for i in range(1, no+1):
        fact = fact * i
    print(f"Process ID : {os.getpid()}, number = {no}, Factorial : {fact}")
    return fact

def main():
    Data = list()
    print("Enter no of elements")
    No = int(input())
    print("Enter elements one by one")

    for i in range(0,No):
        Data.append(int(input()))

    p = multiprocessing.Pool()
    result = p.map(Factorial, Data)

    print(result)
    p.close()
    p.join()

if __name__ == "__main__":
    main()