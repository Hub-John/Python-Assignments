
# Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. 
# Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum.py Name of the function from main python file should be ListPrime().
# Input number of elements  : 11
# Input elements            : 13 5 45 7 4 56 10 34 2 5 8
# Output                    : 54 (13 + 5 + 7 +2 + 5)

import MarvellousNum

def ListPrime(TotalElement):

    Elements = []

    for i in range(TotalElement):
        EachElement = int(input("Enter elements: "))
        Elements.append(EachElement)
    
    sum = 0

    for num in Elements:
        if MarvellousNum.CheckPrime(num):
            sum = sum + num
    return sum


def main():

    TotalElement = int(input("Enter Input numer of elements: "))

    result = ListPrime(TotalElement)

    print(f"Sum of prime numbers is {result}")
 
if __name__ == "__main__":
    main()