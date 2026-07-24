import schedule
import sys
import time

def DisplayMessage(monday, wednesday, friday):

    monday = "Start your weekly goals"
    print(monday)

    wednesday = "Review your weekly progress"
    print(wednesday)

    friday = "Weekly work completed"
    print(friday)
     

def main():

    schedule.every().monday.at("09:00").do(DisplayMessage, sys.argv[1], '','')
    schedule.every().wednesday.at("17:07").do(DisplayMessage, '', sys.argv[2], '')
    schedule.every().friday.at("18:07").do(DisplayMessage, '', '', sys.argv[3])

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()