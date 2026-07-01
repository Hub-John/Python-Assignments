
# Write a program which accepts one number and prints all odd numbers till that number.

def AllOddNumber(first):
    
    OddNum = []

    for no in range(1, first + 1, 2):
        OddNum.append(no)

    return OddNum

    
def main():

    NumberOne = int(input("Enter your Number: "))
    
    Result = AllOddNumber(NumberOne)

    print("Output: ", Result)


if __name__ == "__main__":
    main()