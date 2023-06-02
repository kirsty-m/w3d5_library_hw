from flask import render_template, request, redirect
from app import app
from models.books import books
from models.book import *

@app.route("/books")
def index():
    return render_template("index.html", books=books)

@app.route("/books/<index>")
def show_book_details(index):
    return render_template("book_details.html", book = books[int(index)])

