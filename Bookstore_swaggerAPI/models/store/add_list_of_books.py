from Bookstore_swaggerAPI.models.book_store_base import Book_store_base


class addListOfBooks(Book_store_base):

    def __init__(self, userId, collectionOfIsbns:list):
        self._userId = userId
        self._collectionOfIsbns = collectionOfIsbns

    @property
    def userId(self):
        return self._userId

    @property
    def collectionOfIsbns(self):
        return self._collectionOfIsbns