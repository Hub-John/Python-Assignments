
# Write a program which accepts one character and checks whether it is vowel or consonant.

def checkVowelCons(acceptChar):

    if(acceptChar == "a" or acceptChar == "e" or acceptChar == "i" or acceptChar == "o" or acceptChar == "u"):
        return True
    else:
        return False


def main():
    
    userChar = str(input("Enter your Character: "))

    result = checkVowelCons(userChar)

    if(result == True):
        print("Character is vowel")
    else:
        print("Character is consonant")

if __name__ == "__main__":
    main()