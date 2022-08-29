from Bookstore_swaggerAPI.models.book_store_base import Book_store_base
from Bookstore_swaggerAPI.models.store.book_modal import BookModal


class AllBooksModal():
    def __init__(self, books:dict):
        self._books =list(map(lambda book: BookModal(**book), books["books"]))

    @property
    def books(self):
        return self._books


    def to_json(self):
        return str(list(map(lambda book: book.to_json(), self._books)))
