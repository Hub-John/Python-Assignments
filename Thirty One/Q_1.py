import schedule
import time

def diplay(user_msg, time_interval):

    print("-"*40)
    print(f"{user_msg}\nevery {time_interval} seconds\n")
    print("-"*40)

def main():

    user_msg = input("Enter Message: ")
    time_interval = int(input("Enter interval in seconds: "))

    schedule.every(time_interval).seconds.do(diplay, user_msg, time_interval)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()