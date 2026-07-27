import schedule
import time
import os
import sys

def Display(FileName):

    Ret = False

    Ret = os.path.exists(FileName)

    if(Ret == False):
        print("File does NOT exists")
        return

    Ret = os.path.getsize(FileName)

    if(Ret > 0):

        Ret = os.access(FileName, os.R_OK)
        
        if not Ret:
            print("Permission is denied")
            print("File cannot be opened")
            return
    
        fobj = open(FileName, "r")
        print(fobj.read())
        fobj.close()
        
    else:
        print("File is empty")
        return

        
def main():

    schedule.every(1).minute.do(Display, sys.argv[1])

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()