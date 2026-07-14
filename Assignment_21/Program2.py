import threading

def Max(data):
    max = 0
    for no in data:
        if(max < no):
            max = no
    print("Max element from the list is : ", max)
            
def Min(data):
    min = data[0]
    for no in data:
        if(min > no):
            min = no
    print("Min element from the list is : ", min)

def main():
    Data = list()
    print("Enter the number of elements to be stored in the list")
    No = int(input())
    print("Enter elements one by one")
    for i in range(0, No):
        Data.append(int(input()))

    Thread1 = threading.Thread(target = Max, name = "Thread1", args = (Data,))
    Thread2 = threading.Thread(target = Min, name = "Thread2", args = (Data,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

if __name__ == "__main__":
    main()
