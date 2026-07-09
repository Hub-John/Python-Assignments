
# Write a Python program using multiprocessing.Pool to calculate the sum of all even numbers from 1 to N for every number from the given list.
    # Input Data = [1000000, 2000000, 3000000, 4000000]
    # Expected Task: 
        # For each number N, calculate: 2 + 4 + 6 + ... + N
    # Expected Output Format:
        # Process ID : 1234
        # Input Number : 1000000
        # Sum of Even Numbers : 250000500000

import multiprocessing
import os

def FindEvenNumber(No):

    new_list = []
    
    for i in range(1, No + 1):

        if i % 2 == 0:
            new_list.append(i)
    
    return sum(new_list)


def main():
    
    data_list = [1000000, 2000000, 3000000, 4000000]
    
    pObj = multiprocessing.Pool()

    result = pObj.map(FindEvenNumber, data_list)

    pObj.close()
    pObj.join()

    print(f"PID of the process: {os.getpid()}")
    print(f"Input Numbers: {data_list}")
    print(f"Sum of Even Numbers: {result}")
    

if __name__ == "__main__":
    main()