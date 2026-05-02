from repositories.book_repository import BookRepository
from services.author_service import AuthorService

class BookService:

    def __init__(self, bookRepository: BookRepository, authorService: AuthorService):
        self.bookRepository = bookRepository
        self.authorService= authorService
        
    def add_book(self, title, author_id, publish_year, genre, pages):
        if not title or not title.strip():
            raise ValueError("Book title can not be empty.")
        if pages<=0:
            raise ValueError("No of Pages in a book can not be 0.")
        if publish_year<=0:
            raise ValueError("Publish Year must be a positive integer.")
        try:
            self.authorService.find_author(author_id)
        except LookupError:
            raise ValueError(f"Author with {author_id} does not exist.")
        
        return self.bookRepository.create(title, author_id, publish_year, genre, pages)
    
    def list_books(self):
        return self.bookRepository.get_all()
    
    def find_books(self,book_id):
        book= self.bookRepository.get_by_id(book_id)
        if book is None:
            raise LookupError(f"Bood with id {book_id} not found.")
        return book
    
    def remove_book(self, book_id):
        if not self.bookRepository.delete(book_id): 
            raise LookupError(f"Bood with id {book_id} not found.")
