import math

def FactorialNumber(first):
    return math.factorial(first)
    
def main():

    NumberOne = int(input("Enter your Number: "))
    
    Result = FactorialNumber(NumberOne)

    print("Factorial number is:", Result)

if __name__ == "__main__":
    main()