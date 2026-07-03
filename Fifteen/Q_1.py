
# Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

SquareNumber = lambda num : num * num

def main():

    NumberList = [2, 3, 4, 5, 6, 7]
    
    result = list(map(SquareNumber, NumberList))

    print("Square of:", result)

if __name__ == "__main__":
    main()