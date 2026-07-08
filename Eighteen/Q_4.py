
# Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
# Input number of elements  : 11
# Input elements            : 13 5 45 7 4 56 5 34 2 5 65
# Element to search         : 5
# Output                    : 3

def FrequencyNumber(frequency):

    list = []
    
    for i in range(frequency):
        value = int(input("Enter the elements: "))
        list.append(value)
    
    search = int(input("Enter element to search: "))

    counter = 0
    
    for counter in list:
        if counter == search:
            counter += 1


    return counter

def main():

    userList = int(input("Input number of elements: "))

    result = FrequencyNumber(userList)

    print(result)
       
if __name__ == "__main__":
    main()