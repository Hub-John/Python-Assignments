def main():

    fname = "example.text"
    search_word = "Marvellous"
    Found = False

    with open(fname, "r", encoding="utf-8") as file:
        if search_word in file.read():
            Found = True


    if(Found == True):
        print(f"Found {search_word} character in {fname}")
    else:
        print(f"NOT found {search_word} character")      
    
if __name__ == "__main__":
    main()