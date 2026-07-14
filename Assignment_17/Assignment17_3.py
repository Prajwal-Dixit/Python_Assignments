def Facorial(No):
    fact = 1
    for i in range(1, No+1):
        fact = fact * i
    return fact

def main():
    No = int(input("Enter a number"))
    Ret = Facorial(No)
    print(f"Factorial of {No} is : {Ret}")

if __name__ == "__main__":
    main()