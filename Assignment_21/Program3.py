import threading

cnt = 0
lock = threading.Lock()

def Increment(name, No):
    global cnt
    print(f"{name} is waiting")
    with lock :
        print(f"{name} has aquired the access")
        cnt += 1
        No[0] = cnt
    print(f"{name} has released the lock")

def main():
    No = [0]     #if we write No = [], it raises error at line no 12, as there is no index as 0 at that time
                 #But Now we have created the index 0, so there wont be indexoutof bound error
                 
    Thread1 = threading.Thread(target = Increment, args = ("t1",No,))
    Thread2 = threading.Thread(target = Increment, args = ("t2",No,))
    Thread3 = threading.Thread(target = Increment, args = ("t3",No,))

    Thread1.start()
    Thread2.start()
    Thread3.start()

    Thread1.join()
    Thread2.join()
    Thread3.join()

    print(No)

if __name__ == "__main__":
    main()
