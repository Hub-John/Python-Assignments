
# Write a lambda function which accepts three numbers and returns largest number.

Multiplication = lambda val1, val2, val3 : val1 if (val1 >= val2 and val1 >= val3) else (val2 if val2 >= val3 else val3)

def main():

    RecievedNumberOne = int(input("Enter your first favorite number: "))
    RecievedNumberTwo = int(input("Enter your second favorite number: "))
    RecievedNumberThree = int(input("Enter your third favorite number: "))
    
    result = Multiplication(RecievedNumberOne, RecievedNumberTwo, RecievedNumberThree)

    print("Largest number is:", result)

if __name__ == "__main__":
    main()