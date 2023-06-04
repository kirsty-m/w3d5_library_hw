from flask import render_template, request, redirect
from app import app
from models.books import books, add_new_book, delete_book_by_index
from models.book import *



@app.route("/books")
def index():
    return render_template("index.html", books = books)

@app.route("/books/<index>")
def show_book_details(index):
    return render_template("book_details.html", book = books[int(index)])

@app.route("/books", methods=["POST"])
def add_book():
    book_title = request.form["title"]
    book_author = request.form["author"]
    book_genre = request.form["genre"]
    checked_out = []
    new_book = Book(book_title, book_author, book_genre, checked_out)
    add_new_book(new_book)
    # return render_template("index.html", books = books)
    return redirect("/books")


@app.route("/books/del/<index>", methods=["POST"])
def delete_by_index(index):
    delete_book_by_index(int(index))
    return redirect("/books")
    # return render_template("index.html", books = books)


