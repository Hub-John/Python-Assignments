
# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.

# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

from functools import reduce

def EvenNumber(No):
     return (No % 2 == 0)    

def Squre(No):
    return (No * No)

def Equal(No1, No2):
    return (No1 + No2)

def main():
    
    count = int(input("Enter number of elements :"))

    UserList = []

    for i in range(count):
        UserInput = int((input("Enter number: ")))
        UserList.append(UserInput)
    
    FData = list(filter(EvenNumber, UserList))
    print("Filter Data is: ", FData)

    MData = list(map(Squre, FData))
    print("Map Data is: ", MData)

    RData = reduce(Equal, MData)
    print("Reduce Data is: ", RData)


if __name__ == "__main__":
    main()