
# Design a Python application where multiple threads update a shared variable.
    # Use a Lock to avoid race conditions.
    # Each thread should increment the shared counter multiple times.
    # Display the final value of the counter after all threads complete execution.

import threading

# Shared resources
shared_counter = 0
counter_lock = threading.Lock()

# Configuration
NUM_THREADS = 5
INCREMENTS_PER_THREAD = 100000

def increment_counter(thread_id):
    """Worker function for each thread to safely increment the counter."""
    global shared_counter
    
    for _ in range(INCREMENTS_PER_THREAD):
        # Acquire the lock before modifying the shared variable
        with counter_lock:
            shared_counter += 1
            
    print(f"Thread {thread_id} has finished its increments.")

def main():
    threads = []

    print(f"Starting {NUM_THREADS} threads...")
    print(f"Each thread will increment the counter {INCREMENTS_PER_THREAD:,} times.\n")

    # Create and start threads
    for i in range(NUM_THREADS):
        thread = threading.Thread(target=increment_counter, args=(i + 1,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete execution
    for thread in threads:
        thread.join()

    # Display final results
    expected_value = NUM_THREADS * INCREMENTS_PER_THREAD
    print("\n--- Execution Complete ---")
    print(f"Final Counter Value: {shared_counter:,}")
    print(f"Expected Value:      {expected_value:,}")

if __name__ == "__main__":
    main()
