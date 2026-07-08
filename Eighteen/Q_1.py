
# Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
# Input number of elements  : 6
# Input elements            : 13 5 45 7 4 56
# Output                    : 130

def AdditionElements(CarryData):
    
    sum = 0
    
    for i in CarryData:
        sum = sum + i  
    return sum

def main():

    userList = input("Type your number list here: ")

    numbers_list = [
        int(num) 
        for num in userList.split()
    ]
    
    Result = AdditionElements(numbers_list)

    print("Input number of elements:", len(numbers_list))
    print("Input elements:", userList)
    print("Output:", Result)

if __name__ == "__main__":
    main()