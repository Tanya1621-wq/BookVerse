# crud methods
from models.book import Book

class BookRepository:

    def __init__(self):
        self._books= {}
        self._next_id= 1

    # create
    def create(self,title, author_id, publish_year, genre, pages):
        book= Book(self._next_id, title, author_id,publish_year, genre, pages )
        self._books[self._next_id]= book
        self._next_id+=1
        return book
    
    # read(one)
    def get_by_id(self, book_id):
        return self._books.get(book_id)
    
    # read(all)

    def get_all(self):
        return list(self._books.values())
    
    # update

    def update(self, book_id, title=None, author_id=None, publish_year=None, genre=None, pages=None):
        book= get_by_id(book_id)
        if title is not None:
            book.title= title
        if author_id is not None:
            book.author_id= author_id
        if publish_year is not None:
            book.publish_year= publish_year
        if genre is not None:
            book.genre= genre
        if pages is not None:
            book.pages= pages
        return book
    # delete

    def delete(self, book_id):
        return self._books.pop(book_id, None) is not None
        