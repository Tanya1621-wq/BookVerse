from services.book_service import BookService

class BookMenu:
    """CLI menu for Book CRUD operations."""

    def __init__(self, service: BookService):
        self.service = service
        
    def show(self):
        while True:
            print("\n----- BOOK MENU -----")
            print("1. Add Book")
            print("2. View All Books")
            print("3. View Book by ID")
            print("4. Update Book")
            print("5. Delete Book")
            print("0. Back")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self._add_book()
            elif choice == "2":
                self._view_all()
            elif choice == "3":
                self._view_one()
            elif choice == "4":
                self._update_book()
            elif choice == "5":
                self._delete_book()
            elif choice == "0":
                break
            else:
                print("Invalid choice. Try again.")

    def _add_book(self):
        try:
            title = input("Title: ") 
            author_id = int(input("Author Id: "))
            publish_year = int(input("Publish year: "))
            genre = input("Genre: ")
            pages = int(input("Pages: "))
            book = self.service.add_book(title, author_id,  publish_year, genre, pages)
            print(f"Created -> {book}")
        except ValueError as e:
            print(f"Error: {e}")

    def _view_all(self):
        books = self.service.list_books()
        if not books:
            print("No Books yet.")
            return
        print(f"Total: {len(books)}")
        for a in books:
            print(a)

    def _view_one(self):
        try:
            book_id = int(input("Book ID: "))
            print(self.service.find_books(book_id))
        except ValueError:
            print("ID must be a number.")
        except LookupError as e:
            print(f"Error: {e}")

    def _update_book(self):
        try:
            book_id = int(input("Book ID to update: "))
            print("(Leave blank to keep the current value)")
            author_id = int(input("Author ID to update: "))
            title = input("New name: ") or None
            genre = input("New genre: ") or None
            pages = input("New No of Pages: ") or None
            publish_year = int(publish_year) if publish_year else None
            book = self.service.edit_book(book_id, title, author_id, publish_year, genre,pages)
            print(f"Updated -> {book}")
        except ValueError as e:
            print(f"Error: {e}")
        except LookupError as e:
            print(f"Error: {e}")

    def _delete_author(self):
        try:
            author_id = int(input("Author ID to delete: "))
            confirm = input(f"Delete author {author_id}? (y/n): ").strip().lower()
            if confirm == "y":
                self.service.remove_author(author_id)
                print("Deleted.")
            else:
                print("Cancelled.")
        except ValueError:
            print("ID must be a number.")
        except LookupError as e:
            print(f"Error: {e}")
