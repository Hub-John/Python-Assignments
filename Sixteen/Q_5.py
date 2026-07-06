def Display(No):
    
    for i in range(No):
        print(No-i)

def main():

    UserInput = int(input("Enter is you number:"))

    Result = Display(UserInput)

if __name__ == "__main__":
    main()