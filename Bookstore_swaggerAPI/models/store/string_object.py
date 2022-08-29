from Bookstore_swaggerAPI.models.book_store_base import Book_store_base


class StringObject(Book_store_base):
    def __init__(self, isbn:str, userId:str):
        self._isbn = isbn
        self._userId = userId
