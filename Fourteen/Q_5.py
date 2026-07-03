
# Write a lambda function which accepts one number and returns True if number is even otherwise False.

OddOrEven = lambda val1 : val1 % 2 == 0

def main():

    RecievedNumber = int(input("Enter your first favorite number: "))
    
    result = OddOrEven(RecievedNumber)

    if(result == True):
        print("Number is Even")
    else:
        print("Number is Odd")

if __name__ == "__main__":
    main()