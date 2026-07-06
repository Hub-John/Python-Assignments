def ChkNum(No):
    
    if No % 2 == 0:
        return True
    else:
        return False
    

def main():
    
    UserInput = int(input("Enter the number: "))
    result = ChkNum(UserInput)
    
    if result == True:
        print(f"{UserInput} is Even number")
    else:
        print(f"{UserInput} is Odd number")

if __name__ == "__main__":
    main()