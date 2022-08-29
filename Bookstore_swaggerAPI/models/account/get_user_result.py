from Bookstore_swaggerAPI.models.book_store_base import Book_store_base
from Bookstore_swaggerAPI.models.store.book_modal import BookModal


class GetUserResult(Book_store_base):
    def __init__(self, userId, username, books:list=list):
        self._userId = userId
        self._username = username
        self._books = books

    @property
    def userId(self):
        return self._userId

    @userId.setter
    def userId(self, userId: list):
        self._userId = userId

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def books(self):
        return self._books

    @books.setter
    def books(self, books):
        self._books = books
