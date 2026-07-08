
# Design a Python application that creates two threads.
    # Thread 1 should compute the sum of elements from a list.
    # Thread 2 should compute the product of elements from the same list.
    # Return the results to the main thread and display them.

import threading

def compute_sum(data_list, results_dict):
    total_sum = 0
    for num in data_list:
        total_sum += num
    results_dict['sum'] = total_sum

def compute_product(data_list, results_dict):
    if not data_list:
        results_dict['product'] = 0
        return
        
    total_product = 1
    for num in data_list:
        total_product *= num
    results_dict['product'] = total_product  # Store result under 'product' key

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
    shared_results = {}
    
    thread1 = threading.Thread(target=compute_sum, args=(numbers, shared_results))
    thread2 = threading.Thread(target=compute_product, args=(numbers, shared_results))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print(f"Result from Thread 1 (Sum)    : {shared_results['sum']}")
    print(f"Result from Thread 2 (Product): {shared_results['product']}")

if __name__ == "__main__":
    main()
