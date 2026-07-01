
# Write a program which accepts one number and prints reverse of that number.

def ReverseDigit(rDigit):

    TextRev = ""

    for char in reversed(rDigit):
        TextRev = TextRev + char
    return TextRev

    # ------------------------------------ #

    # count = list(rDigit)
    # updatedCount = list()

    # for char in reversed(count):
    #     updatedCount.append(char)

    # return updatedCount
    
    # ------------------------------------ #
    
def main():
    
    UserInput = input("Enter a whole number one number: ")

    result = ReverseDigit(UserInput)

    print("Reverse digit is: ", result)
    
if __name__ == "__main__":
    main()