
# Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.

from functools import reduce

MaxNumber = lambda val1, val2 : val1 if val1 > val2 else val2

def main():

    NumberList = [1, 4, 3, 64, 5, 45, 7, 8, 9, 15, 104]
    
    result = reduce(MaxNumber, NumberList)

    if(MaxNumber == True):
        print("This is Minimum number:", result)
    else:
        print("This is Maximum number:", result)

if __name__ == "__main__":
    main()