# models.py
class Book:
    def __init__(self, title, author, published_year, isbn, genre=None):
        self.title = title
        self.author = author
        self.published_year = published_year
        self.isbn = isbn
        self.genre = genre

    def to_dict(self):
        """Return book details as a dictionary."""
        return {
            "title": self.title,
            "author": self.author,
            "published_year": self.published_year,
            "isbn": self.isbn,
            "genre": self.genre
        }
