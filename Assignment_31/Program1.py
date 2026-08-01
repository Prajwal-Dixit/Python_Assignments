import schedule
import time

def main():
    message = input("Enter a message \n")
    interval = int(input("Enter a time interval in seconds for displaying the message\n"))

    try:
        while True:
            print(message)
            time.sleep(interval)
    except KeyboardInterrupt as ke:
        print("Program execution terminated", ke)

if __name__ == "__main__":
    main()
