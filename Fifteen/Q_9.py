
# Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

from functools import reduce

ProductEle = lambda x, y: x * y

def main():

    NumbersList = [1, 2, 3, 4, 5]
    
    product_result = reduce(ProductEle, NumbersList)

    print("The product of all elements is:", product_result)

if __name__ == "__main__":
    main()