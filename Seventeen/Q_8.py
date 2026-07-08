
# Write a program which accept one number and display below pattern.

def NumberPattern(No):

    for i in range(1, No + 1):
        
        for j in range(1, i + 1):
            print(j, end=" ")
        print()               
        
def main():

    UserInput = int(input("Enter you favorite number: "))

    result = NumberPattern(UserInput)


if __name__ == "__main__":
    main()