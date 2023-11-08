class Book:
    def __init__(self, book_id, title, author, no_of_pages):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._no_of_pages = no_of_pages


class BookSearchEngine:
    def SearchBookByTitle(self, title):
        pass

    def SearchBookByAuthor(self, author):
        pass