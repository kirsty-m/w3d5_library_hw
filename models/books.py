from models.book import *

book1 = Book("Great Expectations", "Charles Dickens", "Fiction", True)
book2 = Book("Dune", "Frank Herbert", "Sci-fi", False)
book3 = Book("Frankenstein", "Mary Shelley", "Horror", True)

books = [book1, book2, book3]

def add_new_book(book):
    books.append(book)

def delete_book_by_index(index):
    books.pop(index)