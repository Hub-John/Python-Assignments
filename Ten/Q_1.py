
# Write a program which accepts one number and prints multiplication table of that number.

def MultiplicationTable(first):

    List = []

    for no in range(1, 11):
        List.append(first*no)
    
    return List
    
def main():

    NumberOne = int(input("Enter your Number: "))
    
    Result = MultiplicationTable(NumberOne)

    print(Result)

if __name__ == "__main__":
    main()