Min = lambda No1, No2 : No1 if(No1 < No2) else No2

def main():
    print("Enter two numbers")
    No1 = int(input())
    No2 = int(input())
    Ret = Min(No1, No2)
    print("Minimum no is : ",Ret)

if __name__ == "__main__":
    main()