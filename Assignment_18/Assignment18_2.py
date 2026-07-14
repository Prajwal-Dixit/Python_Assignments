def Max(data):
    max = 0
    for no in data:
        if(max < no):
            max = no
    return max

def main():
    Data = list()
    No = int(input("Enter number of elements to be stored in the list "))
    print("Enter the elements one by one")
    for i in range(0, No):
        temp = int(input())
        Data.append(temp)

    Ret = Max(Data)
    print(f"Max element of the list is : {Ret}")

if __name__ == "__main__":
    main()