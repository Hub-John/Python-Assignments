import schedule
import time
import os
import datetime
import sys

def Display(DirName):

    timestamp = time.ctime()
    fobj = open("File_%s.txt"%timestamp, "a")

    for FolderName, SubFolderName, FileName in os.walk(DirName):

        for fname in FileName:
            fobj.write(f"Filename: {fname}\n")

    now = datetime.datetime.now()

    fobj.write(f"Creation date: {now.date()}\n")
    fobj.write(f"Creation time: {now.time()}\n")

    print("Log created successfully")

def main():

    schedule.every(3).minutes.do(Display, sys.argv[1])

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()