import os
import sys

def DirName(DirName, DirFileName):
     
    for FolderName, SubFolderName, FileName in os.walk(DirName, DirFileName):
            
        if(DirName == FolderName):
            print(f"Folder Name: {FolderName}")
        
        for fname in FileName:
            if(DirFileName == fname):
                print(f"File Name : {fname}")

def main():
    
    DirName(sys.argv[1], sys.argv[2])
    
if __name__ == "__main__":
    main()


# Terminal Command : python3 Q_1.py Dir Demo.text