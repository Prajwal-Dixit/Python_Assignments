def DigSum(value):
    Sum = 0
    while(int(value) != 0):
        Sum = Sum + (int(value % 10))
        value = value / 10
    return Sum

def main():
    No = int(input("Enter a number "))
    Ret = DigSum(No)
    print("Sum of the digits is : ",Ret)

if __name__ == "__main__":
    main()