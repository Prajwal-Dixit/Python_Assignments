def ChkEven(No):
    if (No % 2 == 0):
        return True
    else:
        return False

def main():
    No = int(input("Enter a nummber "))
    Ret = ChkEven(No)
    if(Ret == True):
        print("Even number")
    else:
        print("Odd number")

if __name__ == "__main__":
    main()