def Frequency(data, no):
    cnt = 0
    for i in data:
        if(no == i):
            cnt = cnt + 1
    return cnt

def main():
    Data = list()
    No1 = int(input("Enter number of elements to be stored in the list "))
    print("Enter the elements one by one")
    for i in range(0, No1):
        temp = int(input())
        Data.append(temp)
    
    No2 = int(input("Enter number to check its frequency of occurence in the list"))
    Ret = Frequency(Data, No2)
    print(f"Frequency is : {Ret}")

if __name__ == "__main__":
    main()