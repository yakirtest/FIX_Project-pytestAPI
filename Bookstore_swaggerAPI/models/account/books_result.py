from Bookstore_swaggerAPI.models.book_store_base import Book_store_base


class BooksResult(Book_store_base):
    def __init__(self,userId,message):
        self._userId=userId
        self._message = message

    @property
    def userId(self):
        return self._userId

    @userId.setter
    def userId(self,userId):
        self._userId=userId

    @property
    def message(self):
        return self._message

    @message.setter
    def username(self,message):
        self._message=message