from repositories.author_repository import AuthorRepository


class AuthorService:
    """Business logic layer. Validates input before touching the repository."""

    def __init__(self, repository: AuthorRepository):
        self.repository = repository

    def add_author(self, name, country, birth_year):
        if not name or not name.strip():
            raise ValueError("Author name cannot be empty.")
        if not country or not country.strip():
            raise ValueError("Country cannot be empty.")
        if birth_year <= 0:
            raise ValueError("Birth year must be a positive number.")
        return self.repository.create(name.strip(), country.strip(), birth_year)

    def list_authors(self):
        return self.repository.get_all()

    def find_author(self, author_id):
        author = self.repository.get_by_id(author_id)
        if author is None:
            raise LookupError(f"Author with id {author_id} not found.")
        return author

    def edit_author(self, author_id, name=None, country=None, birth_year=None):
        if name is not None and not name.strip():
            raise ValueError("Name cannot be blank.")
        if birth_year is not None and birth_year <= 0:
            raise ValueError("Birth year must be positive.")
        author = self.repository.update(author_id, name, country, birth_year)
        if author is None:
            raise LookupError(f"Author with id {author_id} not found.")
        return author

    def remove_author(self, author_id):
        if not self.repository.delete(author_id):
            raise LookupError(f"Author with id {author_id} not found.")
