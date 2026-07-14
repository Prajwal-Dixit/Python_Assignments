import multiprocessing
import os

def Factorial(no):
    fact = 1
    for i in range(1, no+1):
        fact = fact * i
    return (os.getpid(),fact,no)         #Returning in the form of tuple

def main():
    Data = list()
    process = []
    print("Enter no of elements")
    No = int(input())
    print("Enter elements one by one")

    for i in range(0,No):
        Data.append(int(input()))

    p = multiprocessing.Pool()
    result = p.map(Factorial, Data)   

    for pid, cnt, no in result:
        print(f"Process Id : {pid}, Input number: {no}, Factorial of number : {cnt}")

    p.close()
    p.join()

if __name__ == "__main__":
    main()