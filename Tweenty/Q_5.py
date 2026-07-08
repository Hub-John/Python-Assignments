
# Design a Python application that creates two threads named Thread1 and Thread2.
    # Thread1 should display numbers from 1 to 50.
    # Thread2 should display numbers from 50 to 1 in reverse order.
    # Ensure that:
        # Thread2 starts execution only after Thread1 has completed.
    # Use appropriate thread synchronizatio

import threading

def Thread1(Data):

    numbers_list = [] 

    for i in range(1, Data + 1, 1):
        numbers_list.append(i)
    print(numbers_list)
        
    
def Thread2(Data):
    
    numbers_list = [] 

    for i in range(Data, 1, -1):
        numbers_list.append(i)
    print(numbers_list)

def main():

    Obj1 = threading.Thread(target=Thread1, args=(50, ))
    Obj2 = threading.Thread(target=Thread2, args=(50, ))

    Obj1.start()
    Obj1.join()
    
    Obj2.start()
    Obj2.start()

if __name__ == "__main__":
    main()