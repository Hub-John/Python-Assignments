def Add(No1, No2):
    
    sum = No1 + No2
    return sum

def main():
    
    UserInput1 = int(input("Enter the first number: "))
    UserInput2 = int(input("Enter the second number: "))

    result = Add(UserInput1, UserInput2)
    
    print(f"Addition of {UserInput1} and {UserInput2} is: ", result)

if __name__ == "__main__":
    main()