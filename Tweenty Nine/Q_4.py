import hashlib

def DiffFiles(No1, No2):

    f1obj = open(No1, "rb")
    f2obj = open(No2, "rb")

    hobj1 = hashlib.md5()
    hobj2 = hashlib.md5()

    Buffer1 = f1obj.read(1000)
    Buffer2 = f2obj.read(1000)
    
    while(len(Buffer1) > 0 and len(Buffer2) > 0):
        hobj1.update(Buffer1)
        hobj2.update(Buffer2)
        Buffer1 = f1obj.read(1000)
        Buffer2 = f2obj.read(1000)
    
    if (hobj1.hexdigest() == hobj2.hexdigest()):
        print("Succes")
    else:
        print("Fail")

    f1obj.close()
    f2obj.close()

def main():
    
    result = DiffFiles("Demo.text", "ABC.text")

if __name__ == "__main__":
    main()
