
# Design a Python application that creates two threads named EvenFactor and OddFactor.
    # Both threads should accept one integer number as a parameter.
    # The EvenFactor thread should:
        # Identify all even factors of the given number.
        # Calculate and display the sum of even factors.
    # The OddFactor thread should:
        # Identify all odd factors of the given number.
        # Calculate and display the sum of odd factors.
    # After both threads complete execution, the main thread should display the message: “Exit from main”

import threading

def EvenFactor(No):
    
    EvenList = []
    sum = 0

    for counter in range(2, No + 1):
        if No % counter == 0 and No % 2 == 0:
            EvenList.append(counter)
            sum = sum + counter
    print("Even numbers list: ", EvenList)
    print("Sum of even numbers: ", sum)
    print(f"This is Even TID {threading.get_ident()}")

def OddFactor(No):

    OddList = []
    sum = 0

    for counter in range(1, No + 1, 2):
        OddList.append(counter)
        sum = sum + counter
    
    print("Odd numbers list: ", OddList)
    print("Sum of odd numbers: ", sum)
    print(f"This is odd TID {threading.get_ident()}")

def main():
    print("---------- Start form main --------------")
    print(f"This is Main TID: {threading.get_ident()}")
    print("-----------------------------------------")

    ObjEven = threading.Thread(target=EvenFactor, args=(20, ))
    ObjOdd = threading.Thread(target=OddFactor, args=(20, ))

    ObjEven.start()
    print("-----------------------------------------")
    ObjOdd.start()

    ObjEven.join()
    ObjOdd.join()

    print("---------- Exit form main ---------------")

if __name__ == "__main__":
    main()