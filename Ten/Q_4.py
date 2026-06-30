def AllEvenNumber(first):
    
    EvenNum = []

    for no in range(2, first + 1, 2):
        EvenNum.append(no)

    return EvenNum

    
def main():

    NumberOne = int(input("Enter your Number: "))
    
    Result = AllEvenNumber(NumberOne)

    print("Output: ", Result)


if __name__ == "__main__":
    main()