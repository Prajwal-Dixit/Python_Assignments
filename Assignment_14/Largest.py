Max = lambda No1, No2, No3 : No1 if(No1 > No2 and No1 > No3) else No2 if(No2 > No3 and No2 > No1) else No3

def main():
    print("Enter three numbers")
    No1 = int(input())
    No2 = int(input())
    No3 = int(input())

    Ret = Max(No1, No2, No3)
    print("Largest no is : ",Ret)

if __name__ == "__main__":
    main()