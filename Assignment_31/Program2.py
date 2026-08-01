import schedule
import time

def display_msg(msg):
    print(msg)

def main():
    message = input("Enter a message \n")
    interval = int(input("Enter a time interval in seconds for displaying the message\n"))

    schedule.every(interval).seconds.do(display_msg, message)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt as ke:
        print("Program execution terminated")        

if __name__ == "__main__":
    main()