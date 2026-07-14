import threading

def CountSmall(str):    
    current_thread = threading.current_thread()
    print(f"Thread name is : {current_thread.name} and ID is : {current_thread.ident}")
    cnt = 0
    for ch in str:
        if(ch <= "z" and ch >= "a"):
            cnt = cnt + 1
    print(f"Nummber of Lowercase letters are : {cnt}")

def CountCapital(str):
    current_thread = threading.current_thread()
    print(f"Thread name is : {current_thread.name} and ID is : {current_thread.ident}")
    cnt = 0
    for ch in str:
        if(ch <= "Z" and ch >= "A"):
            cnt = cnt + 1
    print(f"Nummber of Capital letters are : {cnt}")

def CountDigits(str):
    current_thread = threading.current_thread()
    print(f"Thread name is : {current_thread.name} and ID is : {current_thread.ident}")
    cnt = 0
    for ch in str:
        if(ch <= "9" and ch >= "0"):
            cnt = cnt + 1
    print(f"Nummber of digits are : {cnt}")

def main():
    Username = "KingAlexander397"
    Small = threading.Thread(target = CountSmall, args = (Username,))
    Capital = threading.Thread(target = CountCapital, args = (Username,))
    Digits = threading.Thread(target = CountDigits, args = (Username,))
    Small.start()
    Capital.start()
    Digits.start()     

    Small.join()
    Capital.join()
    Digits.join()

    print("Exit from main")

if __name__ == "__main__":
    main()