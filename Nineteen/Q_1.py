
# Write a program which contains one lambda function which accepts one parameter and return power of two.

PowerOf = lambda No1 : No1 * No1 

def main():

    UserInput = int(input("Enter your number: "))
    
    result = PowerOf(UserInput)

    print(f"{result} power of {UserInput}")

if __name__ == "__main__":
    main()