def Pattern(No):
    
    for i in range(No):
        print("* " * No)

def main():

    UserInput = int(input("Enter the number please: "))

    result = Pattern(UserInput)

if __name__ == "__main__":
    main()