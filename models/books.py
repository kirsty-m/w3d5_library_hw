from models.book import *

book1 = Book("Great Expectations", "Charles Dickens", "Fiction")
book2 = Book("Dune", "Frank Herbert", "Sci-fi")
book3 = Book("Frankenstein", "Mary Shelley", "Horror")

books = [book1, book2, book3]

def add_new_book(book):
    books.append(book)