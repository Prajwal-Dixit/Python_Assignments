def NaturalSum(value):
    Sum = 0
    for i in range(1,value+1):
        Sum = Sum + i
    return Sum

def main():
    No = int(input("Enter a number "))
    Ret  = NaturalSum(No)
    print("Sum of ",No," natural numbers is : ", Ret)

if __name__ == "__main__":
    main()

