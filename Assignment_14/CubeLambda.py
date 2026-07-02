Square = lambda No : No * No * No

def main():
    No = int(input("Enter a number "))
    Ret = Square(No)
    print("Cube is : ",Ret)

if __name__ == "__main__":
    main()