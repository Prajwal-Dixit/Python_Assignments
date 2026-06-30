def Odd(value):
    for i in range(1,value+1):
        if(i % 2 != 0):
            print(i)
    

def main():
    No = int(input("Enter a number "))
    Odd(No)

if __name__ == "__main__":
    main()

