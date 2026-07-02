from functools import reduce

Max = lambda No1, No2 : No1 * No2

def main():
    Data = [10,2,3,4,5]
    Ret = reduce(Max, Data)
    print(Ret)
    
if __name__ == "__main__":
    main()