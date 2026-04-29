from models.author import Author


class AuthorRepository:
    """In-memory storage for authors. Later can be swapped with a real DB."""

    def __init__(self):
        self._authors = {}        # author_id -> Author
        self._next_id = 1

    # CREATE
    def create(self, name, country, birth_year):
        author = Author(self._next_id, name, country, birth_year)
        self._authors[self._next_id] = author
        self._next_id += 1
        return author
                                                        
    # READ (all)
    def get_all(self):
        return list(self._authors.values())

    # READ (one)
    def get_by_id(self, author_id):
        return self._authors.get(author_id)

    # UPDATE
    def update(self, author_id, name=None, country=None, birth_year=None):
        author = self._authors.get(author_id)
        if author is None:
            return None
        if name is not None:
            author.name = name
        if country is not None:
            author.country = country
        if birth_year is not None:
            author.birth_year = birth_year
        return author

    # DELETE
    def delete(self, author_id):
        return self._authors.pop(author_id, None) is not None
