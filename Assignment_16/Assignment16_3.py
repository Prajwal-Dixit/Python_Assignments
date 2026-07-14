def Add(No1, No2):
    result = No1 + No2
    return result

def main():
    print("Enter two nummbers ")
    No1 = int(input())
    No2 = int(input())
    Ret = Add(No1, No2)
    print(f"Addition is : {Ret}")

if __name__ == "__main__":
    main()