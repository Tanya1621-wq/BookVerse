class Book:
    def __init__(self, book_id, title, author_id, publish_year, genre, pages):
        self.book_id = book_id
        self.title = title
        self.author_id = author_id
        self.publish_year = publish_year
        self.genre = genre
        self.pages = pages

        def to_dict(self):
            return {
                "book_id": self.book_id,
                "title": self.title,
                "author_id": self.author_id,
                "publish_year": self.publish_year,
                "genre": self.genre,
                "pages": self.pages,
            }
