class Book:
    """A class representing a book with title, author, and availability."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        """Borrow the book if available."""
        if self.available:
            self.available = False
            print(f"'{self.title}' has been borrowed.")
            return True
        else:
            print(f"'{self.title}' is not available for borrowing.")
            return False
    
    def return_book(self):
        """Return the book."""
        if not self.available:
            self.available = True
            print(f"'{self.title}' has been returned.")
            return True
        else:
            print(f"'{self.title}' was not borrowed.")
            return False
    
    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"'{self.title}' by {self.author} - {status}"


class Library:
    """A class representing a library that manages multiple books."""
    
    def __init__(self, name):
        self.name = name
        self.books = []  # List to store Book objects
    
    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)
        print(f"'{book.title}' has been added to {self.name}.")
    
    def search_by_title(self, title):
        """Search for books by title (case-insensitive partial match)."""
        results = [book for book in self.books if title.lower() in book.title.lower()]
        return results
    
    def search_by_author(self, author):
        """Search for books by author (case-insensitive partial match)."""
        results = [book for book in self.books if author.lower() in book.author.lower()]
        return results
    
    def borrow_book(self, title):
        """Borrow a book by title."""
        results = self.search_by_title(title)
        for book in results:
            if book.available:
                book.borrow()
                return True
        print(f"No available book matching '{title}' found.")
        return False
    
    def return_book(self, title):
        """Return a book by title."""
        results = self.search_by_title(title)
        for book in results:
            if not book.available:
                book.return_book()
                return True
        print(f"No borrowed book matching '{title}' found.")
        return False
    
    def display_all_books(self):
        """Display all books in the library."""
        print(f"\n--- All Books in {self.name} ---")
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(f"  {book}")
        print()


# Demonstration
if __name__ == "__main__":
    # Create book objects
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("1984", "George Orwell")
    book4 = Book("Pride and Prejudice", "Jane Austen")
    book5 = Book("The Catcher in the Rye", "J.D. Salinger")
    
    # Create a library
    library = Library("City Public Library")
    
    # Add books to the library
    print("=== Adding Books ===")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)
    
    # Display all books
    library.display_all_books()
    
    # Search by title
    print("=== Searching by Title: 'Great' ===")
    results = library.search_by_title("Great")
    for book in results:
        print(f"  Found: {book}")
    print()
    
    # Search by author
    print("=== Searching by Author: 'Orwell' ===")
    results = library.search_by_author("Orwell")
    for book in results:
        print(f"  Found: {book}")
    print()
    
    # Borrow books
    print("=== Borrowing Books ===")
    library.borrow_book("1984")
    library.borrow_book("Pride and Prejudice")
    
    # Try to borrow an already borrowed book
    print("\n=== Trying to Borrow '1984' Again ===")
    library.borrow_book("1984")
    
    # Display all books after borrowing
    library.display_all_books()
    
    # Return a book
    print("=== Returning Books ===")
    library.return_book("1984")
    
    # Display all books after returning
    library.display_all_books()
    
    # Try to return a book that wasn't borrowed
    print("=== Trying to Return 'The Great Gatsby' (not borrowed) ===")
    library.return_book("The Great Gatsby")
