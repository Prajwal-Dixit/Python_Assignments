def Pattern(No):
    for i in range(1, No+1):
        for j in range(1, No+1):
            if(j <= i):
                print(j ," ", end = " ")
        print()

def main():
    No = int(input("Enter a number "))
    Pattern(No)

if __name__ == "__main__":
    main()