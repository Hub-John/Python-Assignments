def main():

    user_input = input("Enter folder name: ")
    
    with open(user_input, mode='r', encoding='UTF-8') as file:
        content = file.read()
        print(f"{content}")
        
    
if __name__ == "__main__":
    main()