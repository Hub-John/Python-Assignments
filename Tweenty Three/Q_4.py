
# Write a program that counts how many odd numbers exist between 1 and N.
    # Input Data = [1000000, 2000000, 3000000, 4000000]
    # Expected Task: 
        # For each number N, calculate: 1 + 3 + 5 + ... + N
    # Expected Output Format:
        # Process ID : 1234
        # Input Number : 1000000
        # Sum of Odd Numbers : 500000

import multiprocessing
import os

def FindOddNumber(No):

    new_list = []
    
    for i in range(1, No + 1):

        if i % 2 == 1:
            new_list.append(i)
    return len(new_list)


def main():
    
    data_list = [1000000, 2000000, 3000000, 4000000]
    
    pObj = multiprocessing.Pool()

    result = pObj.map(FindOddNumber, data_list)

    pObj.close()
    pObj.join()

    print(f"PID of the process: {os.getpid()}")
    print(f"Input Numbers: {data_list}")
    print(f"Sum of Odd Numbers: {result}")
    

if __name__ == "__main__":
    main()