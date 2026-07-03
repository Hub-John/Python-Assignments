
# Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

CountEverNum = lambda num: num % 2 == 0

def main():

    NumbersList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    
    result = list(filter(CountEverNum, NumbersList))

    print("The count of even number is:", result)

if __name__ == "__main__":
    main()