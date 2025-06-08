# Custom exceptions
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - {status}"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"The book '{book.title}' is already borrowed.")
        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def add_member(self, name):
        self.members.append(Member(name))

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book '{title}' not found in the library.")

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            print(f"Member {member_name} not found.")
            return
        try:
            book = self.find_book(book_title)
            member.borrow_book(book)
            print(f"{member.name} borrowed '{book.title}'.")
        except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
            print(f"Error: {e}")

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            print(f"Member {member_name} not found.")
            return
        try:
            book = self.find_book(book_title)
            member.return_book(book)
            print(f"{member.name} returned '{book.title}'.")
        except BookNotFoundException as e:
            print(f"Error: {e}")

# Example usage:
library = Library()
library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_member("Alice")
library.add_member("Bob")

library.borrow_book("Alice", "1984")
library.borrow_book("Alice", "To Kill a Mockingbird")
library.borrow_book("Alice", "Some Unknown Book")  # Triggers BookNotFoundException
library.borrow_book("Alice", "1984")  # BookAlreadyBorrowedException
library.borrow_book("Alice", "To Kill a Mockingbird")  # BookAlreadyBorrowedException

library.borrow_book("Alice", "New Book")  # Not found
library.borrow_book("Alice", "1984")
library.return_book("Alice", "1984")
library.borrow_book("Alice", "1984")  # Now success again
