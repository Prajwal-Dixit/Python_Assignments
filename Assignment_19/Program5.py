from functools import reduce

def ChkPrime(No):
    if(No == 2):
        return True
    else:
        for i in range(2, No):
            if(No % i == 0):
                return False
            else:
                return True


    
Mult = lambda No : No * 2

Max = lambda No1, No2 : No1 if(No1 > No2) else No2

def main():
    Data = list()
    print("Enter number of elements to be stored in the list :")
    No = int(input())
    print("Enter the elements one by one :")

    for i in range(0, No):
        Data.append(int(input()))

    DataX = list(filter(ChkPrime, Data))
    print(DataX)

    DataXX = list(map(Mult, DataX))
    print(DataXX)

    Result = reduce(Max, DataXX)
    print(Result)

if __name__ == "__main__":
    main()