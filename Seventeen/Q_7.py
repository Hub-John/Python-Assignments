
# Write a program which accept one number and display below pattern.

def NumberPattern(No):

    for i in range(No):
        for i in range(1, No + 1):
            print(i, end=" ")
        print()

def main():

    UserInput = int(input("Enter you favorite number: "))

    result = NumberPattern(UserInput)


if __name__ == "__main__":
    main()