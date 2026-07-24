import sys

def DisplayContent(fileName):

    fobj = open(fileName, "r")
    
    print(fobj.read())

    fobj.close()
    
def main():
    
    DisplayContent(sys.argv[1])
    
if __name__ == "__main__":
    main()


# Terminal Command : python3 Q_2.py Demo.text