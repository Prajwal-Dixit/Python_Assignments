def PrintEven(No):
    cnt = 0
    no = 2
    while(cnt < No):
        if(no % 2 == 0):
            print(no)
            no = no + 2
            cnt = cnt + 1

def main():
    No = int(input("Enter a nummber "))
    PrintEven(No)


if __name__ == "__main__":
    main()