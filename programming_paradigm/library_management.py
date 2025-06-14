class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private by convention

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_checked_out(self):
        return self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only Book instances can be added to the library.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                return
        print(f"Book '{title}' was not checked out.")

    def list_available_books(self):
        for book in self._books:
            if not book.is_checked_out():
                print(f"{book.title} by {book.author}")
