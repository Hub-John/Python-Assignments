
# Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.

def Division(val1, val2):
    result = val1 / val2
    return int(result)

def Multiplication(val1, val2):
    result = val1 * val2
    return result

def Subtraction(val1, val2):
    result = val1 - val2
    return result

def Additon(val1, val2):
    result = val1 + val2
    return result

def ArithmeticOperation(FirstNumber, SecondNumber):
    add = Additon(FirstNumber, SecondNumber)
    print("Addition is:", add)
    sub = Subtraction(FirstNumber, SecondNumber)
    print("Substractin is:", sub)
    mult = Multiplication(FirstNumber, SecondNumber)
    print("Multiplication is:", mult)
    divi = Division(FirstNumber, SecondNumber)
    print("Division is:", divi)
    
    
def main():
    
    FirstNumber = int(input("Enter your First Character: "))

    SecondNumber = int(input("Enter your Second Character: "))

    result = ArithmeticOperation(FirstNumber, SecondNumber)

if __name__ == "__main__":
    main()