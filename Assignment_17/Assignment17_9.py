def DigitCnt(No):
    cnt = 0
    while(No != 0):
        No = int(No / 10)
        cnt = cnt + 1
    return cnt

def main():
    No = int(input("Enter a number "))
    Ret = DigitCnt(No)
    print(f"Number of digits are : {Ret}")

if __name__ == "__main__":
    main()