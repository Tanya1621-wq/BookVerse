class Author:
    def __init__(self, author_id, name, country, birth_year):
        self.author_id = author_id
        self.name = name
        self.country = country
        self.birth_year = birth_year

    def to_dict(self):
        return {
            "author_id": self.author_id,
            "name": self.name,
            "country": self.country,
            "birth_year": self.birth_year,
        }

    def __str__(self):
        return f"[{self.author_id}] {self.name} | {self.country} | born {self.birth_year}"
