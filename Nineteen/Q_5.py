
# 5.Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions)

# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62

from functools import reduce

Multiple = lambda No : No * 2
MaxNumber = lambda No1, No2 : No1 if No1 > No2 else No2

def PrimeNumber(No):

    if No < 2:
        return False
    for i in range(2, int(No**0.5) + 1):
        if No % i == 0:
            return False
    return True 

def main():
    
    # count = int(input("Enter number of elements :"))

    UserList = [2, 70 , 11, 10, 17, 23, 31, 77]

    # for i in range(count):
    #     UserInput = int((input("Enter number: ")))
    #     UserList.append(UserInput)
    
    FData = list(filter(PrimeNumber, UserList))
    print("Filter Data is: ", FData)

    MData = list(map(Multiple, FData))
    print("Map Data is: ", MData)

    RData = reduce(MaxNumber, MData)
    print("Reduce Data is: ", RData)


if __name__ == "__main__":
    main()