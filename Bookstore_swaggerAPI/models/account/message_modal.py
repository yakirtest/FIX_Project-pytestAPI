from Bookstore_swaggerAPI.models.book_store_base import Book_store_base


class MessageModal(Book_store_base):
    def __init__(self,code,message):
        self._code=code
        self._message=message

    @property
    def message(self):
        return self._message

