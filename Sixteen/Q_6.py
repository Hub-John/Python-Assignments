def main():

    UserInput = int(input("Enter is you number:"))

    if UserInput > 0:
        print("Number is Positive'")
    elif UserInput < 0:
        print("Number is Negative'")
    else:
        print("Number is Zero")

if __name__ == "__main__":
    main()