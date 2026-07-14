import multiprocessing
import os

def CntOdd(no):
    cnt = 0
    for i in range(1, no+1):
        if(i % 2 != 0):
            cnt = cnt +1
    return (os.getpid(),cnt,no)         #Returning in the form of tuple

def main():
    Data = list()
    process = []
    print("Enter no of elements")
    No = int(input())
    print("Enter elements one by one")

    for i in range(0,No):
        Data.append(int(input()))

    p = multiprocessing.Pool()
    result = p.map(CntOdd, Data)   #This creates a list of tuples, not just integers
    #This list will look like : [(1012, 192929, 10), (1221, 223221, 20), (2122, 134423, 30)]
    #We can unpack them like : for no1, no2, no3 in result :

    for pid, cnt, no in result:
        print(f"Process Id : {pid}, Input number: {no}, Number of Odd numbers : {cnt}")

    p.close()
    p.join()

if __name__ == "__main__":
    main()