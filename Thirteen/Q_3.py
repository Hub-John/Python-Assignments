
# Write a program which accepts one number and checks whether it is perfect number or not.

def checkPerfectNumber(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
            # print(sum)
    return sum == n

def main():
    
    perfectNumber = int(input("Type your number: "))

    result = checkPerfectNumber(perfectNumber)
   
    if(result == True):
        print("Is a Prime Number")
    else:
         print("Is a NOT Prime Number")


if __name__ == "__main__":
    main()