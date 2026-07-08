
# Design a Python application that creates two threads.
    # Thread 1 should calculate and display the maximum element from an list.
    # Thread 2 should calculate and display the minimum element from the same list.
    # The list should be accepted from the user.

import threading

def MaxNumber(Data, final_result):
    
    current_max = Data[0]

    for max in Data:
        
        if max > current_max:
            current_max = max
    
    final_result[0] = current_max
        
        
def MinNumber(Data, final_result):
    
    current_min = Data[0]

    for min in Data:
        
        if min < current_min:
            current_min = min
    
    final_result[1] = current_min
    
  
def main():
    
    user_list = int(input("Enter total element count: "))
    new_user_list = []

    final_result = [None, None]

    for i in range(user_list):
        each_element = int(input("Enter element:"))
        new_user_list.append(each_element)
    
    Obj1 = threading.Thread(target=MaxNumber, args=(new_user_list, final_result))
    Obj2 = threading.Thread(target=MinNumber, args=(new_user_list, final_result))

    Obj1.start()
    Obj1.join()
    
    Obj2.start()
    Obj2.join()

    print(f"{final_result[0]} is a maximum number of this list")
    print(f"{final_result[1]} is a minimum number of this list")
    
if __name__ == "__main__":
    main()