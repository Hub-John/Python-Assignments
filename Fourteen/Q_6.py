
# Write a lambda function which accepts one number and returns True if number is odd otherwise False.

OddOrEven = lambda val1 : val1 % 2 == 1 

def main():

    RecievedNumber = int(input("Enter your first favorite number: "))
    
    result = OddOrEven(RecievedNumber)

    if(result == True):
        print("Number is Odd")
    else:
        print("Number is Even")

if __name__ == "__main__":
    main()