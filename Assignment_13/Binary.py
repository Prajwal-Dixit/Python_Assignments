def Binary(value):
    Result = list()
    Bin = 0
    while(value != 0):
        Result.append(value % 2)
        value = int(value/2)

    Result.reverse()
    for no in Result:
        Bin = Bin * 10 + no
    return Bin

def main():
    print("Enter a number")
    No = int(input())

    Ret = Binary(No)
    print("Binary converted number is : ",Ret)

if __name__ == "__main__":
    main()
