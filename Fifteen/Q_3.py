
# Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.

OddNumber = lambda num : num % 2 == 1

def main():

    NumberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    result = list(filter(OddNumber, NumberList))

    print("Filter odd numbers:", result)

if __name__ == "__main__":
    main()