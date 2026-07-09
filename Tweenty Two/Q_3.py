
# For every number in the given list, count how many prime numbers exist between 1 and N using multiprocessing Pool.
    # Example
        # 10000
        # 20000
        # 30000
        # 40000
    # Display total prime count for each number.

import multiprocessing

def CheckPrime(n):
    
    if n <= 1:
        return False

    # Check divisibility from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def CountPrimeNumber(n):

    count = 0
    for i in range(1, n + 1):
        if CheckPrime(i):
            count = count + 1
    return count
    
def main():
    
    data_list = [10000, 20000, 30000, 40000]
    
    pObj = multiprocessing.Pool()

    result = pObj.map(CountPrimeNumber, data_list)

    pObj.close()
    pObj.join()

    print(f"Total prime count is: {result}")

if __name__ == "__main__":
    main()