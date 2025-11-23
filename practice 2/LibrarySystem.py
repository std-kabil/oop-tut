class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def display(self):
        status = "Available" if self.is_available else "Not Available"
        print(f"{self.title} by {self.author} - {status}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                print(f"You borrowed '{title}'")
                return
        print("Book not available")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.is_available = True
                print(f"You returned '{title}'")
                return

    def list_available_books(self):
        for book in self.books:
            if book.is_available:
                book.display()


# Create books
b1 = Book("1984", "George Orwell")
b2 = Book("Clean Code", "Robert Martin")
b3 = Book("Harry Potter", "J.K. Rowling")

# Library
lib = Library()
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

lib.borrow("1984")
lib.list_available_books()

lib.return_book("1984")
lib.list_available_books()
