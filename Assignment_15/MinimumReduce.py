from functools import reduce

Min = lambda No1, No2 : No1 if(No1 < No2) else No2

def main():
    Data = [10,2,300,4,5,65,7,8,9,10]
    Ret = reduce(Min, Data)
    print(Ret)
    
if __name__ == "__main__":
    main()