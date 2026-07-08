import Arithmetic

def main():

    UserInput1 = int(input("Enter the first number: "))
    UserInput2 = int(input("Enter the second number: "))

    result1 = Arithmetic.Add(UserInput1, UserInput2)
    print(f"{UserInput1} and {UserInput2} addition is:", result1)
    
    result2 = Arithmetic.Sub(UserInput1, UserInput2)
    print(f"{UserInput1} and {UserInput2} substraction is:", result2)

    result3 = Arithmetic.Mult(UserInput1, UserInput2)
    print(f"{UserInput1} and {UserInput2} multiplication is:", result3)

    result4 = Arithmetic.Div(UserInput1, UserInput2)
    print(f"{UserInput1} and {UserInput2} division is:", result4)


if __name__ == "__main__":
    main()