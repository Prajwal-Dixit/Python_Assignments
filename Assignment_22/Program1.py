#1. Write a program that accepts a list of integers and uses Pool.map()
#to calculate the sum of squares from 1 to N for every element in the
#list.

import multiprocessing

def SumSquare(no):
    sum = 0
    for i in range(1, no+1):
        sum = sum + (i **2)
    return sum

def main():
    Data = list()
    print("Enter no of elements")
    No = int(input())
    print("Enter elements one by one")

    for i in range(0,No):
        Data.append(int(input()))

    p = multiprocessing.Pool()
    result = p.map(SumSquare, Data)

    print(result)
    p.close()
    p.join()

if __name__ == "__main__":
    main()
