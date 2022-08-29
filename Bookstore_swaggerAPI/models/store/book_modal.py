from Bookstore_swaggerAPI.models.book_store_base import Book_store_base


class BookModal(Book_store_base):
    def __init__(self, isbn, title, subTitle, author, publish_date, publisher, pages, description, website):
        self._isbn = isbn
        self._title = title
        self._subTitle = subTitle
        self._author = author
        self._publish_date = publish_date
        self._publisher = publisher
        self._pages = pages
        self._description = description
        self._website = website

    @property
    def isbn(self):
        return self._isbn