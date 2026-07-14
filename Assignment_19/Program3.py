from functools import reduce

ChkRange = lambda No : True if(No >= 70 and No <= 90) else False
Increment = lambda No : No + 10
Product = lambda No1, No2 : No1 * No2

def main():
    Data = list()
    print("Enter number of elements to be stored in the list :")
    No = int(input())
    print("Enter the elements one by one :")

    for i in range(0, No):
        Data.append(int(input()))

    DataX = list(filter(ChkRange, Data))
    print(DataX)

    DataXX = list(map(Increment, DataX))
    print(DataXX)

    Result = reduce(Product, DataXX)
    print(Result)

if __name__ == "__main__":
    main()