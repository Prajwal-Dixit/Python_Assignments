import threading

def DisplayEven():
    cnt = 0
    No = 2
    while(cnt != 10):
        print(No)
        No = No + 2
        cnt = cnt + 1

def DisplayOdd():
    cnt = 0
    No = 1
    while(cnt != 10):
        print(No)
        No = No + 2
        cnt = cnt + 1

def main():
    Even = threading.Thread(target = DisplayEven)
    Odd = threading.Thread(target = DisplayOdd)
    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

if __name__ == "__main__":
    main()
