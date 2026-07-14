def ListAdd(data):
    sum = 0
    for no in data:
        sum = sum + no
    return sum

def main():
    Data = list()
    No = int(input("Enter number of elements to be stored in the list "))
    print("Enter the elements one by one")
    for i in range(0, No):
        temp = int(input())
        Data.append(temp)

    Ret = ListAdd(Data)
    print(f"Addition of digits in list is : {Ret}")

if __name__ == "__main__":
    main()
