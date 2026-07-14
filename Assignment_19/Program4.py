from functools import reduce

ChkEven = lambda No : True if(No % 2 == 0) else False
Square = lambda No : No * No
Addition = lambda No1, No2 : No1 + No2

def main():
    Data = list()
    print("Enter number of elements to be stored in the list :")
    No = int(input())
    print("Enter the elements one by one :")

    for i in range(0, No):
        Data.append(int(input()))

    DataX = list(filter(ChkEven, Data))
    print(DataX)

    DataXX = list(map(Square, DataX))
    print(DataXX)

    Result = reduce(Addition, DataXX)
    print(Result)

if __name__ == "__main__":
    main()