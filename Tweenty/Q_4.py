
# Design a Python application that creates three threads named Small, Capital, and Digits.
    # All threads should accept a string as input.
    # The Small thread should count and display the number of lowercase characters.
    # The Capital thread should count and display the number of uppercase characters.
    # The Digits thread should count and display the number of numeric digits.
    # Each thread must also display:
        # Thread ID
        # Thread Name

import threading

def Small(Data):

    lowercase_text = []
    
    for char in Data:
        if char.islower():
            lowercase_text.append(char)
    
    print("Total lower character in this sentance is:", len(lowercase_text))
    print(lowercase_text)
    print(f"TID: {threading.get_ident()} and Name: {threading.current_thread()}")
    
def Capital(Data):
    
    uppercase_text = []
    
    for char in Data:
        if char.isupper():
            uppercase_text.append(char)
    
    print("Total Upper character in this sentance is:", len(uppercase_text))
    print(uppercase_text)
    print(f"TID: {threading.get_ident()} and Name: {threading.current_thread()}")

def Digits(Data):
    
    digitCount = []
    
    for char in Data:
        if char.isdigit():
            digitCount.append(char)
    
    print("Total Digit in this sentance is:", len(digitCount))
    print(digitCount)
    print(f"TID: {threading.get_ident()} and Name: {threading.current_thread()}")

def main():

    data_str = "Learning PYTHON is Fun123, and Practice Makes You Better."

    ObjSmall = threading.Thread(target=Small, args=(data_str, ))
    ObjCapital = threading.Thread(target=Capital, args=(data_str, ))
    ObjDigits = threading.Thread(target=Digits, args=(data_str, ))

    ObjSmall.start()
    ObjCapital.start()
    ObjDigits.start()

    ObjSmall.join()
    ObjCapital.join()
    ObjDigits.join()

    print(f"Name: {threading.current_thread().name} and TID: {threading.get_ident()}")

if __name__ == "__main__":
    main()