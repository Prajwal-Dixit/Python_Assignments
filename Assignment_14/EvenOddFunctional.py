ChkEven = lambda No : True if(No % 2 == 0) else False 

def main():
    print("Enter a numbers")
    No = int(input())

    if(ChkEven(No)):
        print("No is Even")
    else:
        print("No is Odd")

if __name__ == "__main__":
    main()