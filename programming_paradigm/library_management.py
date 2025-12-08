class Book:
    """A class representing a book."""
    
    def __init__(self, title, author):
        """Initialize a new book with title and author, and set it as available (not checked out)."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available (not checked out)."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is available, otherwise False."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book in the format 'title by author'."""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library."""
    
    def __init__(self):
        """Initialize an empty library with a list of books."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it's available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """Return a book by title to the library."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """Print all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(book)
