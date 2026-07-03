
# Write a lambda function which accepts one number and returns cube of that number.

CubeNumber = lambda num : num * num * num

def main():

    RecievedNumber = int(input("Enter your favorite number: "))
    
    result = CubeNumber(RecievedNumber)

    print("Cube of:", result)

if __name__ == "__main__":
    main()