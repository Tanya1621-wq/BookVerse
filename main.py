from repositories.author_repository import AuthorRepository
from repositories.book_repository import BookRepository
from services.author_service import AuthorService
from cli.author_menu import AuthorMenu
from repositories.book_repository import BookRepository
from services.book_service import BookService
from cli.book_menu import BookMenu


def main():
    # Wire dependencies (follow the same pattern for Books later)
    author_repo = AuthorRepository()
    author_service = AuthorService(author_repo)
    author_menu = AuthorMenu(author_service)

    book_repo = BookRepository()
    book_service = BookService(book_repo,AuthorService)
    book_menu = BookMenu(book_service)

    while True:
        print("\n======= BOOK STUDY APP =======")
        print("1. Manage Authors")
        print("2. Manage Books")   # <-- Add this once BookMenu is built
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            author_menu.show()
        elif choice == "2":
           book_menu.show()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
