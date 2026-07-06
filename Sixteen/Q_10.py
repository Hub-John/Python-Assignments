def Display(char):
    
    for i in char:
        return char

def main():

    UserInput = input("Enter the Name: ")

    result = Display(UserInput)

    print(len(result))

if __name__ == "__main__":
    main()