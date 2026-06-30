def ChkPrime(value):
    for i in range(2,value):
        if(value % i == 0):
            return False
        else:
            return True

def main():
    No = int(input("Enter a number "))
    Ret = ChkPrime(No)
    if(Ret == True):
        print("Prime nummber")
    else:
        print("Not a prime number")

if __name__ == "__main__":
    main()