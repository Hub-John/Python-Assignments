def SquareNumber(first):

    squareNum = first * first

    return squareNum
    
    
def main():

    NumberOne = int(input("Enter your Number: "))

    Result = SquareNumber(NumberOne)

    print("Output:", Result)
    

if __name__ == "__main__":
    main()