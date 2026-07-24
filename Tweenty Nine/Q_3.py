import sys

def CopyFileContent(fileName):

    fobj = open(fileName, "r")
    FullContent = fobj.read()

    cobj = open("ABC.text", "w")
    cobj.write(FullContent)
    
    cobj.close()
    fobj.close()
    
def main():
    
    CopyFileContent(sys.argv[1])
    
if __name__ == "__main__":
    main()


# Terminal Command : python3 Q_3.py Demo.text