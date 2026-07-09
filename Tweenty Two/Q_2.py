
# Write a program that calculates factorials of multiple numbers simultaneously using Pool.map().
    # Example Input: [10,15,20,25]
    # Display: Process ID, Input Number, Factorial

import multiprocessing, os

def factorials(No):
    ans = 1

    for i in range(1, No+1):
        ans = ans * i
    return ans

def main():
    
    data_list = [10,15,20,25]
    
    pObj = multiprocessing.Pool()

    result = pObj.map(factorials, data_list)

    pObj.close()
    pObj.join()

    print(f"Running with PID: {os.getpid()}")
    print(f"Input data is: {data_list}")
    print(f"Factorial is: {result}")

if __name__ == "__main__":
    main()