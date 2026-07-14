import threading

def SumEvenFactors(No):
    sum = 0
    for i in range(1, No+1):
        if(No % i == 0 and i % 2 == 0):
            sum = sum + i
    print(sum)

def SumOddFactors(No):
    sum = 0
    for i in range(1, No+1):
        if(No % i == 0 and i % 2 != 0):
            sum = sum + i
    print(sum)

def main():
    No = int(input("Enter a number"))
    EvenFactor = threading.Thread(target = SumEvenFactors, args = (No,))
    OddFactor = threading.Thread(target = SumOddFactors, args = (No,))
    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("Exit from main")

if __name__ == "__main__":
    main()