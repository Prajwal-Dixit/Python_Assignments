def DigCount(value):
    i = 0
    while(int(value) != 0):
        value = value / 10
        i = i + 1
    return i

def main():
    No = int(input("Enter a number "))
    Ret = DigCount(No)
    print("Number of digits are : ",Ret)

if __name__ == "__main__":
    main()