import schedule
import os
import shutil
import pathlib
import sys
import time

def Display(source, destination):

    Ret = True

    if(Ret == os.path.exists(source) and Ret == os.path.isdir(source) and Ret == os.path.exists(destination) and Ret == os.path.isdir(destination)):

        sourceFiles = pathlib.Path(source).rglob("*.txt")
        count = 0

        for textFile in sourceFiles:
            shutil.copy(textFile, destination)
        
            logobj = open("log.txt", "a")
            logobj.write(str(textFile)+"\n")
            count = count + 1
        
        print(f"Total file Copied: {count}")

    else:
       
       print("Directory is NOT present")

    return
        
def main():

    schedule.every(3).seconds.do(Display, sys.argv[1], sys.argv[2])

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()