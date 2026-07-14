def ChkPrime(No):
    for i in range(2, No):
        if(No % i == 0):
            break
        else:
            continue
    
    if(i == No-1):
        return True
    else:
        return False

def main():
    No = int(input("Enter a number "))
    Ret = ChkPrime(No)
    if(Ret == True):
        print("Given no is Prime")
    else:
        print("Given no is not a Prime")


if __name__ == "__main__":
    main()