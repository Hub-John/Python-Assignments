
# Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

DivisiableNumber = lambda val1 : val1 % 3 == 0 and val1 % 5 == 0

def main():

    NumberList = [1, 4, 3, 64, 5, 45, 7, 8, 9, 15, 104]
    
    result = list(filter(DivisiableNumber, NumberList))

    print(result)

if __name__ == "__main__":
    main()