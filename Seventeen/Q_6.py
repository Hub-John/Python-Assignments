
# Write a program which accept one number and display below pattern.

def Pattern(No):
    
    for i in range(1, No+1):
        print("* " * i)

def main():

    UserInput = int(input("Enter the number please: "))

    result = Pattern(UserInput)

if __name__ == "__main__":
    main()