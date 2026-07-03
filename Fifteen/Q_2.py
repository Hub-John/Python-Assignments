
# Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.

EvenNumber = lambda num : num % 2 == 0

def main():

    NumberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    result = list(filter(EvenNumber, NumberList))

    print("Filter even numbers:", result)

if __name__ == "__main__":
    main()