import Arithmatic as am

def main():
    print("Enter two numbers")
    No1 = int(input())
    No2 = int(input())

    Ret = am.Addition(No1, No2)
    print("Addition of the numbers is : ",Ret)

    Ret = am.Subtraction(No1, No2)
    print("Subtraction of the numbers is : ",Ret)

    Ret = am.Multiplication(No1, No2)
    print("Multiplication of the numbers is : ",Ret)

    Ret = am.Division(No1, No2)
    print("Division of the numbers is : ",Ret)

if __name__ == "__main__":
    main()