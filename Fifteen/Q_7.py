
# Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

lengthChar = lambda val1 : len(val1) > 5

def main():

    FruitList = ["Apple", "Mango", "Papaya", "Pineapple", "Guava", "Watermelon", "Banana"]
    
    result = list(filter(lengthChar, FruitList))

    print(result)

if __name__ == "__main__":
    main()