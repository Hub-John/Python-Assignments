import datetime

def DisplayData():

    timenow = datetime.datetime.now()
    
    fobj = open("Marvellous.txt",'a',encoding = 'utf-8')

    fobj.write(f"Task executed at: {timenow}"+"\n")

    fobj.close()
    
def main():
    
    DisplayData()
    
if __name__ == "__main__":
    main()