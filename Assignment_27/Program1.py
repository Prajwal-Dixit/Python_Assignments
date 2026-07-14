class BookStore:
    NoOfBooks = 0
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books : {BookStore.NoOfBooks}")

book1 = BookStore("Python","Rossum")
book1.Display()

book2 = BookStore("Atoms", "Jacob")
book2.Display()
