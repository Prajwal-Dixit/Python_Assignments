def Factorial(value):
    mul = 1
    for i in range(1,value+1):
        mul = mul * i
    return mul

def main():
    No = int(input("Enter a number "))
    Ret = Factorial(No)
    print("Factorial of ",No," is ",Ret)

if __name__ == "__main__":
    main()

