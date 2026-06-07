from models.book import Book

class BookRepository:
    def __init__(self):
        self._books={}
        self.next_id= 1

    def create(self, title, author_id, publish_year, genre, pages):
        book= Book(self.next_id, title, author_id, publish_year, genre, pages)
        self._books[self.next_id]= book
        self.next_id +=1
        return book

    def get_all(self):
        return list(self._books.values())

    def get_by_id(self, book_id):
        return self._books.get(book_id)

    def delete(self, book_id):
        return self._books.pop(book_id, None) is not None

    def update(self, book_id, title=None, author_id=None, publish_year=None, genre=None, pages=None):
        book= self._book(book_id)
        if title is not None:
            self.title= title
        if author_id is not None:
            self.author_id= author_id
        if publish_year is not None:
            self.publish_year= publish_year
        if genre is not None:
            self.genre= genre
        if pages is not None:
            self.pages= pages
        return book


