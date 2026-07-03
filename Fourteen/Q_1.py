
# Write a lambda function which accepts one number and returns square of that number.

SquareNumber = lambda num : num * num

def main():

    RecievedNumber = int(input("Enter your favorite number: "))
    
    result = SquareNumber(RecievedNumber)

    print("Square of:", result)

if __name__ == "__main__":
    main()