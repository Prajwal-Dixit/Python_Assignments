Mult = lambda No1, No2 : No1 * No2

def main():
    print("Enter two numbers")
    No1 = int(input())
    No2 = int(input())
    Ret = Mult(No1, No2)
    print("Multiplication is : ",Ret)

if __name__ == "__main__":
    main()