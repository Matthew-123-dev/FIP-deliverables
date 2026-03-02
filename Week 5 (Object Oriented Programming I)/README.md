# Week 5: Object Oriented Programming I

## Overview

This week introduces **Object-Oriented Programming (OOP)** in Python. The project demonstrates core OOP concepts by building a simple library management system with two classes: `Book` and `Library`.

## Concepts Covered

- **Classes and Objects** - Defining blueprints and creating instances
- **Attributes** - Instance variables to store object state
- **Methods** - Functions that define object behavior
- **Encapsulation** - Bundling data and methods together
- **Composition** - Using objects within other objects (Library contains Books)

## Project Structure

```
Week 5 (Object Oriented Programming I)/
├── app.py      # Main program with Book and Library classes
└── README.md   # This file
```

## Classes

### Book Class

Represents a book with the following:

| Attribute | Type | Description |
|-----------|------|-------------|
| `title` | str | The title of the book |
| `author` | str | The author of the book |
| `available` | bool | Whether the book is available (default: `True`) |

| Method | Description |
|--------|-------------|
| `borrow()` | Marks the book as borrowed if available |
| `return_book()` | Marks the book as available if borrowed |

### Library Class

Manages a collection of books using a list:

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | str | The name of the library |
| `books` | list | A list of `Book` objects |

| Method | Description |
|--------|-------------|
| `add_book(book)` | Adds a book to the library |
| `search_by_title(title)` | Searches for books by title (partial match) |
| `search_by_author(author)` | Searches for books by author (partial match) |
| `borrow_book(title)` | Borrows an available book by title |
| `return_book(title)` | Returns a borrowed book by title |
| `display_all_books()` | Displays all books and their status |

## Usage

### Running the Program

```bash
python3 app.py
```

### Example Code

```python
# Create book objects
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")

# Create a library
library = Library("City Public Library")

# Add books to the library
library.add_book(book1)
library.add_book(book2)

# Search for books
results = library.search_by_author("Orwell")

# Borrow and return books
library.borrow_book("1984")
library.return_book("1984")

# Display all books
library.display_all_books()
```

### Sample Output

```
=== Adding Books ===
'The Great Gatsby' has been added to City Public Library.
'1984' has been added to City Public Library.

--- All Books in City Public Library ---
  'The Great Gatsby' by F. Scott Fitzgerald - Available
  '1984' by George Orwell - Available

=== Borrowing Books ===
'1984' has been borrowed.

=== Returning Books ===
'1984' has been returned.
```

## Key Takeaways

1. **Classes** are blueprints for creating objects with shared attributes and methods
2. **`__init__`** is the constructor method that initializes object attributes
3. **`self`** refers to the current instance of the class
4. **Methods** can modify object state and return values
5. **Composition** allows complex systems to be built from simpler objects
