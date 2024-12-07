from flask import Blueprint, request, jsonify
from .models import Book

bp = Blueprint('api', __name__)
library = []


@bp.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(
        title=data.get('title'),
        author=data.get('author'),
        published_year=data.get('published_year'),
        isbn=data.get('isbn'),
        genre=data.get('genre')
    )
    library.append(new_book)
    return jsonify(new_book.to_dict()), 201


@bp.route('/books', methods=['GET'])
def get_books():
    return jsonify([book.to_dict() for book in library]), 200


@bp.route('/books/search', methods=['GET'])
def search_books():
    author = request.args.get('author')
    published_year = request.args.get('published_year')
    genre = request.args.get('genre')

    filtered_books = [book for book in library if
                      (author is None or book.author == author) and
                      (published_year is None or book.published_year == published_year) and
                      (genre is None or book.genre == genre)
                      ]
    return jsonify([book.to_dict() for book in filtered_books]), 200


@bp.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    data = request.json
    for book in library:
        if book.isbn == isbn:
            book.title = data.get('title', book.title)
            book.author = data.get('author', book.author)
            book.published_year = data.get(
                'published_year', book.published_year)
            book.genre = data.get('genre', book.genre)
            return jsonify(book.to_dict()), 200
    return jsonify({"error": "Book not found"}), 404


@bp.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    global library
    library = [book for book in library if book.isbn != isbn]
    return jsonify({"message": "Book deleted"}), 200
