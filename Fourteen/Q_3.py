
# Write a lambda function which accepts two numbers and returns maximum number.

MaximumNumber = lambda val1, val2 : val1 if val1 > val2 else val2

def main():

    RecievedNumberOne = int(input("Enter your first favorite number: "))
    RecievedNumberTwo = int(input("Enter your second favorite number: "))
    
    result = MaximumNumber(RecievedNumberOne, RecievedNumberTwo)

    if(MaximumNumber == True):
        print("This is Minimum number:", result)
    else:
        print("This is Maximum number", result)


if __name__ == "__main__":
    main()