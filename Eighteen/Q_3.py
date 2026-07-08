
# Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
# Input number of elements  : 4
# Input elements            : 13 5 45 7 4 56 5 34 2 5 65
# Output                    : 5

def MinNumber(maxnumber):

    current_min = maxnumber[0]

    for i in maxnumber:

        if i < current_min:     
            current_min = i 
    
    return current_min
            
def main():

    userList = input("Type your number list here: ")

    numbers_list = [
        int(num) 
        for num in userList.split()
    ]
    
    Result = MinNumber(numbers_list)

    print(Result)
   
if __name__ == "__main__":
    main()