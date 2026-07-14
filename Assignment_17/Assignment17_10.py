def DigitCnt(No):
    sum = 0
    digit = 0
    while(No != 0):
        digit = No % 10
        sum = sum + digit
        No = int(No / 10)
    return sum

def main():
    No = int(input("Enter a number "))
    Ret = DigitCnt(No)
    print(f"Number of digits are : {Ret}")

if __name__ == "__main__":
    main()