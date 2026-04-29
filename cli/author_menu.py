from services.author_service import AuthorService


class AuthorMenu:
    """CLI menu for Author CRUD operations."""

    def __init__(self, service: AuthorService):
        self.service = service
        
    def show(self):
        while True:
            print("\n----- AUTHOR MENU -----")
            print("1. Add Author")
            print("2. View All Authors")
            print("3. View Author by ID")
            print("4. Update Author")
            print("5. Delete Author")
            print("0. Back")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self._add_author()
            elif choice == "2":
                self._view_all()
            elif choice == "3":
                self._view_one()
            elif choice == "4":
                self._update_author()
            elif choice == "5":
                self._delete_author()
            elif choice == "0":
                break
            else:
                print("Invalid choice. Try again.")

    def _add_author(self):
        try:
            name = input("Name: ")
            country = input("Country: ")
            birth_year = int(input("Birth year: "))
            author = self.service.add_author(name, country, birth_year)
            print(f"Created -> {author}")
        except ValueError as e:
            print(f"Error: {e}")

    def _view_all(self):
        authors = self.service.list_authors()
        if not authors:
            print("No authors yet.")
            return
        print(f"Total: {len(authors)}")
        for a in authors:
            print(a)

    def _view_one(self):
        try:
            author_id = int(input("Author ID: "))
            print(self.service.find_author(author_id))
        except ValueError:
            print("ID must be a number.")
        except LookupError as e:
            print(f"Error: {e}")

    def _update_author(self):
        try:
            author_id = int(input("Author ID to update: "))
            print("(Leave blank to keep the current value)")
            name = input("New name: ") or None
            country = input("New country: ") or None
            birth_input = input("New birth year: ").strip()
            birth_year = int(birth_input) if birth_input else None
            author = self.service.edit_author(author_id, name, country, birth_year)
            print(f"Updated -> {author}")
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
