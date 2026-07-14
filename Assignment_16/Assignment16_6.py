def ChkNo(No):
    if (No > 0):
        return "Positive"
    elif (No < 0):
        return "Negative"
    else:
        return "Zero"

def main():
    No = int(input("Enter a number "))
    Ret = ChkNo(No)
    print(f"The number is {Ret}")

if __name__ == "__main__":
    main()