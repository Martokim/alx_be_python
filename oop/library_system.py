class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}" 

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author) # initialize the base class usng super()
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author) # initialize the base class using super()
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []  # Initialize an empty list to store books

    def add_book(self, book):
        self.books.append(book)  # Add a book to the library

    def list_books(self):
        for book in self.books:
            print(book)   # Print each book's details
# Example usage:
# if __name__ == "__main__":
#     my_library = Library()
#     my_library.add_book(Book("1984", "George Orwell"))    
#     my_library.add_book(EBook("Digital Fortress", "Dan Brown", 2.5))
#     my_library.add_book(PrintBook("The Great Gatsby", "F. Scott Fitzgerald", 180))