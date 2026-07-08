
# Write a program which accept number from user and return number of digits in that number.

def CountDigits(No):
    
    total_count = 0

    for char in No:
        total_count = total_count + 1

    return total_count

        
def main():

    UserInput = input("Enter you favorite number: ")

    result = CountDigits(UserInput)

    print(result)

if __name__ == "__main__":
    main()