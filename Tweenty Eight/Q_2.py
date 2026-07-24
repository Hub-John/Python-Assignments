def main():
    fname = "example.text"
    with open(fname, mode='r', encoding='UTF-8') as file:
        content = file.read()
        print(f"Total number of words in {fname} : {len(content)}")
    
if __name__ == "__main__":
    main()