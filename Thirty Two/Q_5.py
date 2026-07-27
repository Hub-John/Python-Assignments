import schedule
import os
import shutil
import pathlib
import sys
import time

def RemoveEmptyFile(DirectoryName):

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):

        for fname in FileName:

            full_path = os.path.join(FolderName, fname)

            if(os.path.getsize(full_path) == 0):
            
                logobj = open("Deleted_File_log.text", "a")
                logobj.write(full_path+"\n")
                os.remove(full_path)
                print("Empty File Removed")
                logobj.close()
            else:
                print("Sorry ! not found empty files")   
        
def main():

    schedule.every(1).hour.do(RemoveEmptyFile, sys.argv[1])

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()