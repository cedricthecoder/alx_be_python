class Book:
    """Base class for a book."""
    
    def __init__(self, title, author):
        """Initialize the Book instance with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Class for eBooks, inherits from Book."""
    
    def __init__(self, title, author, file_size):
        """Initialize the EBook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Class for print books, inherits from Book."""
    
    def __init__(self, title, author, page_count):
        """Initialize the PrintBook with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Library class to manage a collection of books."""
    
    def __init__(self):
        """Initialize the Library with an empty book list."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the library."""
        self.book
