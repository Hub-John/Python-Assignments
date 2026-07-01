
# Write a program which accepts one number and prints sum of first N natural numbers.

def NaturalNumber(first):

    NaturalNumberResult = int((first * (first + 1)) / 2)

    return NaturalNumberResult
    
    
def main():

    NumberOne = int(input("Enter your Number: "))
    
    Result = NaturalNumber(NumberOne)

    print("N natural number is:", Result)

if __name__ == "__main__":
    main()