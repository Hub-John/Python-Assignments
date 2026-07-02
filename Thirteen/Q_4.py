
# Write a program which accepts one number and prints binary equivalent.

def decToBinary(n):
    binArr = []

    while n > 0:
        bit = n % 2
        binArr.append(str(bit))
        n //= 2

    binArr.reverse()
    return "".join(binArr)

def main():
    
    UserNumber = int(input("Type your number: "))

    result = decToBinary(UserNumber)

    print("Output:", result)

if __name__ == "__main__":
    main()