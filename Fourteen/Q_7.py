
# Write a lambda function which accepts one number and returns True if divisible by 5.

DivisibleByFive = lambda val1 : val1 % 5 == 0

def main():

    RecievedNumber = int(input("Enter your first favorite number: "))
    
    result = DivisibleByFive(RecievedNumber)

    if(result == True):
        print("Number is Divisible")
    else:
        print("Number is NOT Divisible")

if __name__ == "__main__":
    main()