
# Write a program which accepts one number and prints cube of that number.

def CubeNumber(first):

    cubeNum = first * first * first

    return cubeNum
    
    
def main():

    NumberOne = int(input("Enter your Number: "))

    Result = CubeNumber(NumberOne)

    print("Output:", Result)
    

if __name__ == "__main__":
    main()