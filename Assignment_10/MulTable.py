def MulTable(value):
    for i in range(1,11):
        print(value * i)

def main():
    No = int(input("Enter a number "))
    MulTable(No)

if __name__ == "__main__":
    main()