def Numbers(value):
    for i in range(value, 0, -1):
        print(i)

def main():
    No = int(input("Enter a number"))
    Numbers(No)

if __name__ == "__main__":
    main()