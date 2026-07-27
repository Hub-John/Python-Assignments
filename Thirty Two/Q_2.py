import schedule
import time
import os
import datetime
import sys

def Display(DirName):

    Ret = True

    if(Ret == os.path.exists(DirName) and Ret == os.path.isdir(DirName)):

        fobj = open("FileSizeLog.txt", "a")

        for FolderName, SubFolderName, FileName in os.walk(DirName):

            for fname in FileName:
                fname = os.path.join(FolderName, fname)
                fobj.write(f"File Path: {fname}\n")
                fobj.write(f"File Size: {os.path.getsize(fname)} bytes\n")
                fobj.write(f"Date and Time: {datetime.datetime.today()}\n")
                fobj.write(f"-"*50+"\n")

        print("Log created successfully")
    else:
       print("Directory is NOT present")
    return
        
def main():

    schedule.every(30).seconds.do(Display, sys.argv[1])

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()