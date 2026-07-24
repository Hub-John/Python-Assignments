def main():

    fname = "example.text"
    
    with open(fname, mode='r', encoding='UTF-8') as file:
        content = file.read()

    fobj = open("example_new.text", "w")

    fobj.write(content)
    print("Copy all contents from the *** example.text *** file into the *** example_new.text *** file.")

    fobj.close()       
    
if __name__ == "__main__":
    main()