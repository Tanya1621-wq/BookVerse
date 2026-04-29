# Book Study App

A small Python CRUD learning project — no database, just in-memory data structures.

## How to run

```bash
cd book_study_app
python main.py
```

## Project Structure

```
book_study_app/
├── main.py                       # App entry point (wires everything)
├── models/
│   └── author.py                 # Author data class
├── repositories/
│   └── author_repository.py      # In-memory storage + raw CRUD
├── services/
│   └── author_service.py         # Business rules / validation
└── cli/
    └── author_menu.py            # Author menu & user interaction
```

## The 4 Layers (important to understand)

| Layer            | Responsibility                                          | Example                 |
|------------------|---------------------------------------------------------|-------------------------|
| **Model**        | Describes the shape of a thing                          | `Author` class          |
| **Repository**   | Stores & retrieves data (acts like a fake database)     | `AuthorRepository`      |
| **Service**      | Validates input, applies business rules                 | `AuthorService`         |
| **CLI / UI**     | Talks to the user                                       | `AuthorMenu`            |

Data flows: `CLI -> Service -> Repository -> Model`

## Adding Books (task)

Mirror exactly the same structure:

1. `models/book.py` → `Book` class (fields: `book_id`, `title`, `author_id`, `pages`, `published_year`)
2. `repositories/book_repository.py` → in-memory dict, CRUD methods
3. `services/book_service.py` → validation (e.g., title not empty, pages > 0, author_id must exist)
4. `cli/book_menu.py` → menu like AuthorMenu
5. In `main.py` → wire `BookRepository`, `BookService`, `BookMenu` and add option `2. Manage Books`

**Bonus challenge:** Inside `BookService`, inject `AuthorService` so before creating a book you can verify the `author_id` exists.
