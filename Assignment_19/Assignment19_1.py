#  Write a program which contains one lambda function which accepts one parameter and return
#  power of two.

Power = lambda No : 2 ** No

def main():
    No = int(input("Enter a number "))
    Result = Power(No)
    print(Result)

if __name__ == "__main__":
    main()
