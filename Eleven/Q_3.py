
# Write a program which accepts one number and prints sum of digits.

def SumOfDigit(sumcount):
    
    convertIntStr = list(sumcount)
    print(convertIntStr)
    sum = 0
    
    for char in convertIntStr: #1
        sum = sum + int(char) 

    return sum

        
def main():
    
    UserInput = input("Enter a whole number one number: ")

    result = SumOfDigit(UserInput)

    print("Sum of digit is: ", result)
    
if __name__ == "__main__":
    main()