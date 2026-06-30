def ReverseNO(value):
    Result = 0

    while(int(value) != 0):
        digit = int(value % 10)
        print(digit)
        Result = Result * 10 + digit
        value = value / 10

    return Result

def ChkPalindrome(value1):

    value2 = ReverseNO(value1)
    if(value1 == value2):
        return True
    else:
        return False

def main():
    No = int(input("Enter a number "))
    Ret = ChkPalindrome(No)
    if(Ret == True):
        print("Number is palindrome")
    else:
        print("Number is not a palindrome")

if __name__ == "__main__":
    main()