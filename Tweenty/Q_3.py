
# Design a Python application that creates two threads named EvenList and OddList.
    # Both threads should accept a list of integers as input.
    # The EvenList thread should:
        # Extract all even elements from the list.
        # Calculate and display their sum.
    # The OddList thread should:
        # Extract all odd elements from the list.
        # Calculate and display their sum.
    # Threads should run concurrently.

import threading

def EvenList(CustomList):
    
    NewList = []
    sum = 0

    for i in CustomList:
        if i % 2 == 0:
            NewList.append(i)
            sum = sum + i
            
    print(sum)
    print(f"This is Even TID {threading.get_ident()}")

def OddList(CustomList):

    NewList = []
    sum = 0

    for i in CustomList:
        if i % 2 == 1:
            NewList.append(i)
            sum = sum + i
    print(sum)
    print(f"This is odd TID {threading.get_ident()}")

def main():
    # print(f"This is Main TID: {threading.get_ident()}")

    List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    ObjEven = threading.Thread(target=EvenList, args=(List, ))
    ObjOdd = threading.Thread(target=OddList, args=(List, ))

    ObjEven.start()
    ObjOdd.start()

if __name__ == "__main__":
    main()