
# Write a program which accept one number form user and return addition of its factors.

# Factor Formula: 1 + 2 + 3 + 4 + 6
# Input = 12
# Output = 16

def Factor(No):
    sum = 0
    
    for i in range(1, No):
        if No % i == 0:
           sum = sum + i
    return sum

def main():

    UserInput = int(input("Enter the number please: "))

    result = Factor(UserInput)

    print(result)
    
if __name__ == "__main__":
    main()