def main():

    fname = "Demo.text"
    search_word = "Marvellous"
    Found = False

    with open(fname, "r", encoding="utf-8") as file:

        content = file.read()

        if search_word in content:
            Found = True

        frequency = content.count(search_word)


    if(Found == True):
        print(f"Found --{search_word}-- character in {fname} file {frequency} times")
    else:
        print(f"NOT found {search_word} character")      
    
if __name__ == "__main__":
    main()