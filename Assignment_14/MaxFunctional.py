max = lambda No1, No2 : No1 if(No1 > No2) else No2

def main():
    print("Enter two numbers")
    No1 = int(input())
    No2 = int(input())
    Ret = max(No1, No2)
    print("Highest no is : ",Ret)

if __name__ == "__main__":
    main()