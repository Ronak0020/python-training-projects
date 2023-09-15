# ========================================= MULTI BOOK INFO ===============================================

class Books:
    books = {}

    def display(self, id):
        if self.books.get(id) == None:
            print("Book was not found! Please re check the ID you entered.")
        print(f"Book name: {self.books[id]['name']}\nAuthor: {self.books[id]['author']}")
        input("\nPress enter to continue...")

    def entry(self, id, name, author):
        if self.books.get(id) == None:
            self.books[id] = {}
        self.books[id]["name"] = name
        self.books[id]["author"] = author

    def entryFunction(self):
        name = input("Enter the name of the book: ")
        author = input("Enter the name of author: ")
        id = int(input("ID for this book: "))
        self.entry(id, name, author)
        print("Book entry has been updated!")
        input("\nPress enter to continue...")

book = Books()

while True:
    MODE = int(input("\nWhat would you like to do?\n[1] Book Entry\n[2] View Book Info\n[3] Exit\n\nEnter reply: "))

    if MODE == 1:
        book.entryFunction()
    elif MODE == 2:
        id = int(input("ID for the book: "))
        book.display(id)
    elif MODE == 3:
        exit()

# ========================================= MULTI BOOK INFO END ===============================================