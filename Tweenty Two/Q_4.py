
# Write a program that calculates
    # 1^5+2^5+3^5+.....+N^5
    # for multiple values of N simultaneously using Pool.
    # Input
        # 100000
        # 200000
        # 300000
        # 400000
    # Measure total execution time.

import multiprocessing, time

def FifthPowers(No):
    
    total = 0

    for i in range(1, No + 1):
        total = i**5
    return total
    
def main():
    
    data_list = [10000, 20000, 30000, 40000]
    
    start_time = time.perf_counter()

    pObj = multiprocessing.Pool()

    result = pObj.map(FifthPowers, data_list)

    pObj.close()
    pObj.join()

    end_time = time.perf_counter()

    print(f"Power of 5 for: {result}")
    print(f"Total time required: {end_time-start_time:.4f}")

if __name__ == "__main__":
    main()