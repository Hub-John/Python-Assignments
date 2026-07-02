
# Write a program which accepts one number and prints its factors.

def factors(acceptNumber):
    
    for i in range(1, acceptNumber + 1):

        if(acceptNumber % i == 0):
            print(i)
        
    return acceptNumber


def main():
    
    userNumber = int(input("Enter your Character: "))

    factors(userNumber)

if __name__ == "__main__":
    main()