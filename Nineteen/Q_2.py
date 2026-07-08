
# Write a program which contains one lambda function which accepts two parameters and return its multiplication.

Multiplication = lambda No1, No2 : No1 * No2

def main():

    UserInputOne = int(input("Enter number: "))
    UserInputTwo = int(input("Enter number: "))

    Result = Multiplication(UserInputOne, UserInputTwo)

    print(f"Multiplication of {UserInputOne} and {UserInputTwo} is: {Result}")


if __name__ == "__main__":
    main()