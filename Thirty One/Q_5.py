import os
import datetime
import schedule
import sys
import time

def DetailsofFolder(dName):

    lobj = open("DirectoryCountLog.txt", "a")

    for FolderName , SubFolder, FileName in os.walk(dName):

            ftotal = []
            timeStamp = datetime.datetime.now()

    
            for fname in FileName:
                ftotal.append(fname) 

            lobj.write(f"Directory path: {FolderName}\n" )
            lobj.write(f"Number of files: {len(ftotal)}\n")
            lobj.write(f"Date and Time: {timeStamp}\n")
            lobj.write("-----------------------------------------------\n")
            print("Log File Created Successfully")

def main():

    schedule.every(5).minutes.do(DetailsofFolder, (sys.argv[1]))

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()