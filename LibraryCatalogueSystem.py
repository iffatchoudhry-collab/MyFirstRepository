class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author
        self.is_available=True

    def checkout(self):
        if self.is_available:
            self.is_available=False
            print(f"'{self.title} has been checked out successfully.")

        else:
            print(f"Sorry, '{self.title}' is not available")

    def return_book(self):
        if not self.is_available:
            self.is_available=True
            print(f"'{self.title} has been returned successfuly")

        else:
            print(f"'{self.title} was already in the Library")

    def ck_status(self):
        status="Available" if self.is_available else "Checked Out"
        return f"Title: {self.title} | Author: {self.author} | Status: {status}"

class BookDatabase:
    def __init__(self):
        self.books=[]

    def add_book(self, book:Book):
        self.books.append(book)
        print("Successfully added Book", book.title)

    def display_all(self):
        if not self.books:
            print("The database is Empty")
            return
        print("\n--------Current Books Record---------")
        for book in self.books:
            book.display_info()
        print("--------------------------------------------\n")

def main():
    db=BookDatabase()
    book1=Book("Canada","Dunya")
    book2=Book("Fun Facts", "Fact")
    db.add_book(book1)
    db.add_book(book2)
    
    db.display_all



    name=input("Enter Book name:  \n")
    author=input("Enter Author's Name: \n")
    new_book=Book(name,author)
    db.add_book(new_book)

    print(db.display_all)
    #Check Out

    book1.checkout()
    print("Book Checked Out", book1.ck_status)

    #Return

    book1.return_book()
    print("Book Returned", book1.ck_status)


main()