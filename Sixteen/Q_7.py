def Divisible(No):

    if No % 5 == 0:
        return True

def main():

    UserInput = int(input("Enter is you number:"))

    Result = Divisible(UserInput)

    if Result == True:
        print(f"{UserInput} is divisible by 5")
    else:
        print(f"{UserInput} is NOT divisible by 5")

if __name__ == "__main__":
    main()