def Factors(value):
    Result = list()
    for i in range(1,value + 1):
        if((value % i) == 0):
            Result.append(i)
    return Result

def main():
    No = int(input("Enter a number"))
    Ret = Factors(No)
    print("Factors of the number are : ", *Ret)

if __name__ == "__main__":
    main()