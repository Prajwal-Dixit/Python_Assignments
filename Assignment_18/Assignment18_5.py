import MarvellousNum as mn

def ListPrime(data):
    Primes = ""
    sum = 0
    for no in data:
        Ret = mn.ChkPrime(no)
        if(Ret == True):
            sum = sum + no
            Primes = Primes + " + " + str(no)
    return sum, Primes

def main():
    Data = list()
    No1 = int(input("Enter number of elements to be stored in the list "))
    print("Enter the elements one by one")
    for i in range(0, No1):
        temp = int(input())
        Data.append(temp)
    
    Ret1, Ret2 = ListPrime(Data)
    print(Ret1,"(", Ret2, ")")

if __name__ == "__main__":
    main()