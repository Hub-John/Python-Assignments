import schedule
import time

def DisplayMessage(message):
    print(message)

def main():

    user_msg = input("Enter Message: ")

    schedule.every(5).seconds.do(DisplayMessage, user_msg)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()