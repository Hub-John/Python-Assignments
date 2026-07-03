
# Write a lambda function which accepts two numbers and returns multiplication.

Multiplication = lambda val1, val2 : val1 * val2

def main():

    RecievedNumberOne = int(input("Enter your first favorite number: "))
    RecievedNumberTwo = int(input("Enter your second favorite number: "))
    
    result = Multiplication(RecievedNumberOne, RecievedNumberTwo)

    print("Total of two number is:", result)

if __name__ == "__main__":
    main()