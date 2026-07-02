
# Write a program which accepts one number and prints that many numbers in reverse order.

def ManyNumbers(AcceptValue):

    list = []

    for i in range(1, AcceptValue + 1):
        list.append(i)
    
    print(list)
    return list


def main():
    
    OneNumber = int(input("Enter your number: "))
    
    result = ManyNumbers(OneNumber)

    updateList = []

    for char in reversed(result):
        updateList.append(char)
    
    print(updateList)
    return updateList

if __name__ == "__main__":
    main()