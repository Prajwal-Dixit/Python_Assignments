def FactorAddition(No):
    sum = 0
    for i in range(1, int(No/2)+1):
        if(No % i == 0):
            sum = sum + i
    return sum

def main():
    No = int(input("Enter a number "))
    Ret = FactorAddition(No)
    print(f"Addition of factors of {No} is : {Ret}")

if __name__ == "__main__":
    main()