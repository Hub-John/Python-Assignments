import sys
import schedule
import shutil
import time

def SourceDestination(source, destination):

    shutil.copy(source, destination)

    flogs = open("backup_log.txt", "a")

    RightNow = time.ctime()

    flogs.write(f"Data_{RightNow}.txt\n")

    print(f"Backup completed successfully at {RightNow}")

def main():

    schedule.every(1).hour.do(SourceDestination, sys.argv[1], sys.argv[2])

    while True:
        schedule.run_pending()

    
if __name__ == "__main__":
    main()