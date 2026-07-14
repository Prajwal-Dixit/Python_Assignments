import threading

def SumEven(data):
    sum = 0
    for no in data:
        if(no % 2 == 0):
            sum = sum + no
    print(sum)

def SumOdd(data):
    sum = 0
    for no in data:
        if(no % 2 != 0):
            sum = sum + no
    print(sum)

def main():
    Data = [10,11,12,13,14,15,16,17,18,19,20]
    Even = threading.Thread(target = SumEven, args = (Data,))
    Odd = threading.Thread(target = SumOdd, args = (Data,))
    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

    print("Exit from main")

if __name__ == "__main__":
    main()