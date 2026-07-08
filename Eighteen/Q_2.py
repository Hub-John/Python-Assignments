
# Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
# Input number of elements  : 7
# Input elements            : 13 5 45 7 4 56 34
# Output                    : 56

def MaxNumber(maxnumber):

    current_max = maxnumber[0]

    for i in maxnumber:

        if i > current_max:     # 13 > 13    5 > 13      45 > 13     7 > 45      4 > 45      56 > 45     34 > 56
            current_max = i     # 13 = 0     13 = 1      45 = 2      45 = 3      45 = 4      56 = 5      56 = 6
    
    return current_max      #56
            
def main():

    userList = input("Type your number list here: ")

    numbers_list = [
        int(num) 
        for num in userList.split()
    ]
    
    Result = MaxNumber(numbers_list)

    print(Result)
   
if __name__ == "__main__":
    main()