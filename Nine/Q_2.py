def CheckGreaterNumber(first, second):

    if(first >= second):
        return True
    else:
        return False
    
def main():

    FirstNumber = int(input("Enter your first Number:"))
    SecondNumber = int(input("Enter your second Number:"))

    Result = CheckGreaterNumber(FirstNumber, SecondNumber)

    if(Result == True):
        print("First number is greter")
    else:
        print("Second number is greter")

if __name__ == "__main__":
    main()