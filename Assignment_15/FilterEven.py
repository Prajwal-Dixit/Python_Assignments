isEven = lambda No: (No % 2 == 0)

def main():
    Data = [1,2,3,4,5,6,7,8,9,10]
    Ret = list(filter(isEven, Data))
    print(Ret)

if __name__ == "__main__":
    main()