Divisible = lambda No : True if(No % 5 == 0) else False 

def main():
    print("Enter a number")
    No = int(input())
    Ret = Divisible(No)
    if(Ret):
        print("No is divisible by 5")
    else:
        print("No is not divisible by 5")

if __name__ == "__main__":
    main()