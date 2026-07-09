
# Write a program that accepts a list of integers and uses Pool.map() to calculate the sum of squares from 1 to N for every element in the list.
    # Example Input: [1000000,2000000,3000000,4000000]
    # Expected Output: [333333833333500000, 2666668666667000000, ...]

import multiprocessing, os

def SumOfSqure(No):
    # print("Process is running with PID : ",os.getpid())
    sum = 0
    
    for i in range(1, No+1):
        sum = sum + (i + i + i + i)
    return sum

def main():
    
    data_list = [1000000,2000000,3000000,4000000]
    result = []

    pObj = multiprocessing.Pool()
    result = pObj.map(SumOfSqure, data_list)

    pObj.close()
    pObj.join()
    
    print(result)

if __name__ == "__main__":
    main()