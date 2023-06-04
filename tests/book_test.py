import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("Great Expectations", "Charles Dickens", "Fiction", True)
        

    def test_book_has_title(self):
        self.assertEqual("Great Expectations", self.book1.title)

    def test_book_has_author(self):
        self.assertEqual("Charles Dickens", self.book1.author)

    def test_book_has_genre(self):
        self.assertEqual("Fiction", self.book1.genre)

    def test_book_checked_out(self):
        self.assertEqual(True, self.book1.checked_out)