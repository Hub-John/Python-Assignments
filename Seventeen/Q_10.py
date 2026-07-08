
# Write a program which accept number from user and return addition of digits in that number.

def DigitsAddition(No):
    
    sum = 0

    for i in str(No):
        sum = sum + int(i)

    return sum 
        
def main():

    UserInput = int(input("Enter you favorite number: "))

    result = DigitsAddition(UserInput)

    print(result)

if __name__ == "__main__":
    main()