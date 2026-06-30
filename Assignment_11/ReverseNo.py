def ReverseNO(value):
    # No = list()
    Result = 0

    while(int(value) != 0):
        digit = int(value % 10)
        Result = Result * 10 + digit
        # No.append(digit)
        value = value / 10

    return Result

def main():
    No = int(input("Enter a number "))
    Ret = ReverseNO(No)
    print("Reversed digits are : ",Ret)

if __name__ == "__main__":
    main()
