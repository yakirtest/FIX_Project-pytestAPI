from Bookstore_swaggerAPI.models.book_store_base import Book_store_base


class TokenViewModel(Book_store_base):
    def __init__(self,token,expires,status,result):
        self._token=token
        self._expires=expires
        self._status=status
        self._result=result

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, token):
        self._token = token

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self,result):
        self._result=result

