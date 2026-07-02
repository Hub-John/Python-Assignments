
# Write a program which accepts one number and prints that many numbers starting from 1.

def ManyNumbers(AcceptValue):

    for i in range(1, AcceptValue + 1):
        print(i)
    return i


def main():
    
    OneNumber = int(input("Enter your number: "))
    
    result = ManyNumbers(OneNumber)

if __name__ == "__main__":
    main()