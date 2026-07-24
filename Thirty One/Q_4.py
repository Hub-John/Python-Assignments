import datetime
import schedule
import time

def CreateLogFile():

    timestamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        
    LogFileName = "MarvellousLog_%s.text"%(timestamp)

    cobj = open(LogFileName, "w")

    cobj.write("Log file created successfully.\n")
    cobj.write(f"Creation Time: {timestamp}")
    
    cobj.close()

def main():

    schedule.every(10).minutes.do(CreateLogFile)

    while True:
         schedule.run_pending()
         time.sleep(1)

if __name__ == "__main__":
    main()