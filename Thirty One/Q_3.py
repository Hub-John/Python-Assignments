import os
import datetime
import schedule
import sys
import time

def DetailsofFolder(dName):

    for FolderName , SubFolder, FileName in os.walk(dName):
    
            print("Directory Scanned: ", FolderName)
            total = []
            ftotal = []
            time = datetime.datetime.now()
            am_pm = time.strftime("%p")
    
            for subf in SubFolder:
                total.append(subf)
            print("Total Subdirectories: ", len(total))
            
    
            for fname in FileName:
                ftotal.append(fname)
    
            print("Total Files: ", len(ftotal))
            print(f"Scan Time: {time} {am_pm}")
            return

def main():

    schedule.every(1).minute.do(DetailsofFolder, (sys.argv[1]))

    while True:
         schedule.run_pending()
         time.sleep(1)

if __name__ == "__main__":
    main()