
# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.

# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000

from functools import reduce

def Inbetween(FunUserList):
     return (FunUserList >= 70 and FunUserList <= 90)    

def Increase(FunUserList):
    return (FunUserList + 10)

def Equal(FunUserList1, FunUserList2):
    return (FunUserList1 * FunUserList2)

def main():
    
    count = int(input("Enter number of elements :"))

    UserList = []

    for i in range(count):
        UserInput = int((input("Enter number: ")))
        UserList.append(UserInput)
    
    FData = list(filter(Inbetween, UserList))
    print("Filter Data is: ", FData)

    MData = list(map(Increase, FData))
    print("Map Data is: ", MData)

    RData = reduce(Equal, MData)
    print("Reduce Data is: ", RData)


if __name__ == "__main__":
    main()