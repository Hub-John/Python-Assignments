
# Write a program which accept one number for user and check whether number is prime or not.

# Numbers less than or equal to 1 are not prime
# 2 is the only even prime number
# Exclude all other even numbers

def Prime(No):

    if No <= 1:
        return False
    
    for i in range(2, No):
        if No % i == 0:
            return False
        
    return True
    

def main():

    UserInput = int(input("Enter the number please: "))

    result = Prime(UserInput)

    if result == True:
        print("This is a prime number")
    else:
        print("This is NOT prime number")

    
if __name__ == "__main__":
    main()