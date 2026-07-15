class BookStore:

    NoOfBooks = 0

    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author

        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.Name} by {self.Author} and No of books: {BookStore.NoOfBooks}")


def main():

    bobj1 = BookStore("C Progamming", "Author One")
    bobj1.Display()

    bobj2 = BookStore("C++ Progamming", "Author Two")
    bobj2.Display()

    bobj3 = BookStore("Javascript", "Author Three")
    bobj3.Display()

    bobj4 = BookStore("HTML/CSS", "Author four")
    bobj4.Display()

    bobj5 = BookStore("React", "Author Five")
    bobj5.Display()
    
    
if __name__ == "__main__":
    main()