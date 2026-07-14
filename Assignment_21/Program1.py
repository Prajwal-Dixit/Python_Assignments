import threading

def DisplayPrime(data):
    for no in data:
        if(no == 2):
            print(no, end = " ")
        else:
            for i in range(2, no):
                if(no % i == 0):
                    break

            if(i == no-1):
                print(no, end = " ")
    print()

        
            
def DisplayNonPrime(data):   
    for no in data:
        for i in range(2, no):
            if(no % i == 0):
                print(no,end = " ")
                break
    print()

def main():
    Data = [2,3,4,5,6,7,8,11,13,18,20,33,23]
    Thread1 = threading.Thread(target = DisplayPrime, name = "Thread1", args = (Data,))
    Thread2 = threading.Thread(target = DisplayNonPrime, name = "Thread2", args = (Data,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
