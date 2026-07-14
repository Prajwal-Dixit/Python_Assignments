import threading

def Sum(data, result):
    sum = 0
    for no in data:
        sum = sum + no
    result["Addition"] = sum
            
def Product(data, result):
    mult = 1
    for no in data:
        mult = mult * no
    result["Product"] = mult

def main():
    Data = list()
    result = {}
    print("Enter the number of elements to be stored in the list")
    No = int(input())
    print("Enter elements one by one")
    for i in range(0, No):
        Data.append(int(input()))

    Thread1 = threading.Thread(target = Sum, name = "Thread1", args = (Data,result,))
    Thread2 = threading.Thread(target = Product, name = "Thread2", args = (Data,result,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print(f"Addition of all the elements is : {result['Addition']}")
    print(f"Product of all the elements is : {result['Product']}")

if __name__ == "__main__":
    main()
