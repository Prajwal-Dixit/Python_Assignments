def ChkDivisible(value):
    if(value % 3 == 0 and value % 5 == 0):
        return True
    else:
        return False
    
def main():
    No = int(input("Enter a number "))

    Ret = ChkDivisible(No)

    if(Ret == True):
        print("Number is divisible by 3 and 5")
    else:
        print("Number is not divisible by 3 and 5")

if __name__ == "__main__":
    main()