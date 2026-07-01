
# Write a program which accepts one number and checks whether it is prime or not.

def is_prime(n):
    
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if n <= 3:
        return True   # 2 and 3 are prime numbers
    if n % 2 == 0 or n % 3 == 0:
        return False  # Exclude all even numbers and multiples of 3

    return True  # No factors found, it is prime

def main():
    # Accept input from the user and convert to an integer
    number = int(input("Enter a whole number to check: "))
    
    # Check and print the result
    if is_prime(number):
        print(f"Output: {number} is a PRIME number.")
    else:
        print(f"Output: {number} is NOT a prime number.")

if __name__ == "__main__":
    main()
