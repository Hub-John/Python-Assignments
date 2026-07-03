
# Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.

from functools import reduce

AdditonNumber = lambda num, val1 : num + val1

def main():

    NumberList = [1, 4, 3, 4, 5, 6, 7, 8, 9, 15]
    
    result = reduce(AdditonNumber, NumberList)

    print("Addition of all numbers:", result)

if __name__ == "__main__":
    main()