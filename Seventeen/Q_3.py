
# Write a program which accept one number from user and return its factorial.

# Factorial Formula: 1 * 2 * 3 * 4 * 5
# Input: 5 
# Output: 120

def Factorial(No):
   
    Fact = 1
    
    for i in range(1, No+1):
        Fact = Fact * i

    return Fact

def main():

    UserInput = int(input("Enter the number please: "))

    result = Factorial(UserInput)

    print(result)
    
if __name__ == "__main__":
    main()