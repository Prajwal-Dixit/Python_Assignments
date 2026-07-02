from functools import reduce

Add = lambda No1, No2: No1 + No2

def main():
    Data = [1,2,3,4,5,6,7,8,9,10]
    Ret = reduce(Add, Data)
    print(Ret)
    
if __name__ == "__main__":
    main()
