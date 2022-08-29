import random

from Bookstore_swaggerAPI.models.book_store_base import Book_store_base


class LoginViewModel(Book_store_base):

    def __init__(self, userName, password):
        self._userName = userName
        self._password = password

    def new_userName(self):
        self._userName+=str(random.randint(0, 1000))

    @property
    def username(self):
        return self._userName
