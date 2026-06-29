def divisibleNumber(first):

    if(first % 3 == 0 and first % 5 == 0):
        return True
    else:
        return False
    
    
def main():

    NumberOne = int(input("Enter your Number: "))

    Result = divisibleNumber(NumberOne)

    if(Result == True):
        print("Divisible by 3 and 5")
    else:
        print("This is not divisible by 3 and 5")


if __name__ == "__main__":
    main()