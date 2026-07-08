
# Design a Python application that creates two threads named Prime and NonPrime.
    # Both threads should accept a list of integers.
    # The Prime thread should display all prime numbers from the list.
    # The Non Prime thread should display all non-prime numbers from the list.

import threading

def Prime(Data):
    
    Elements = []
    sum = 1

    for num in Data:
       
        if num <= 1:
            continue
        
        if num % 2 == 0:
            continue
        
        if num % 2 == 1:
            Elements.append(num)

        sum += num
    
    print(Elements)
    print(f"This is Prime: {threading.get_ident()}")

def NonPrime(Data):
    
    Elements = []
    sum = 1

    for num in Data:
       
        if num <= 1:
            Elements.append(num)
        
        if num % 2 == 0:
            Elements.append(num)
        
        if num % 2 == 1:
            continue

        sum += num
    
    print(Elements)
    print(f"This is NON Prime: {threading.get_ident()}")

def main():
    
    use_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    Obj1 = threading.Thread(target=Prime, args=(use_list, ))
    Obj2 = threading.Thread(target=NonPrime, args=(use_list, ))

    Obj1.start()
    Obj1.join()
    
    Obj2.start()
    Obj2.join()

if __name__ == "__main__":
    main()