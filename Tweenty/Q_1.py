
# Design a Python application that creates two separate threads named Even and Odd.
    # The Even thread should display the first 10 even numbers.
    # The Odd thread should display the first 10 odd numbers.
    # Both threads should execute independently using the threading module.
    # Ensure proper thread creation and execution.

import threading
import time

def Odd(No):

    OddList = []

    for counter in range(1, No + 1, 2):
        OddList.append(counter)
    print(OddList) 
    print(f"This is odd TID {threading.get_ident()}")

def Even(No):
    
    EvenList = []

    for counter in range(2, No + 1, 2):
        EvenList.append(counter)
    print(EvenList)
    print(f"This is Even TID {threading.get_ident()}")


def main():
    print(f"This is Main TID {threading.get_ident()}")
    
    time_start = time.perf_counter()

    ObjOdd = threading.Thread(target=Odd, args=(20, ))
    ObjEven = threading.Thread(target=Even, args=(20, ))

    ObjOdd.start()
    ObjEven.start()

    ObjOdd.join()
    ObjEven.join()

    time_end = time.perf_counter()

    print(f"Total time taken: {time_end-time_start:.4f}" )

if __name__ == "__main__":
    main()