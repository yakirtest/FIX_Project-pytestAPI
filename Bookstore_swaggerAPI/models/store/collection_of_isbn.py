from Bookstore_swaggerAPI.models.book_store_base import Book_store_base


class CollectionOfIsbn(Book_store_base):
    def __init__(self,isbns):
        self._isbns=isbns["books"]

    @property
    def isbns(self):
        return self._isbns
