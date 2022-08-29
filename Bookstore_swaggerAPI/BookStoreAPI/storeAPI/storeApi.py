from Bookstore_swaggerAPI.BookStoreAPI.api_base import Api_Base
from Bookstore_swaggerAPI.models.account.message_modal import MessageModal
from Bookstore_swaggerAPI.models.store.add_list_of_books import addListOfBooks
from Bookstore_swaggerAPI.models.store.all_books_modal import AllBooksModal
from Bookstore_swaggerAPI.models.store.book_modal import BookModal
from Bookstore_swaggerAPI.models.store.collection_of_isbn import CollectionOfIsbn
from Bookstore_swaggerAPI.models.store.string_object import StringObject


class StoreApi(Api_Base):

    def get_books(self):
        """
        function:Find all the books in the store
        :return:AllBooksModal
        """
        res = self._session.get(url=f"{self._url}/BookStore/v1/Books")
        books=res.json()
        if res.status_code == 200:
            return AllBooksModal(books)
        else:
            return res.status_code


    def post_list_books(self,listbook:addListOfBooks,headers:str):
        """
        function: Adds a list of books to the user by
        :param listbook:addListOfBooks
        :param headers:str
        :return:CollectionOfIsbn||status_code
        """
        res = self._session.post(url=f"{self._url}/BookStore/v1/Books", json=listbook.to_json(),headers=headers)
        if res.status_code == 201:
            return CollectionOfIsbn(res.json())
        else:
            return res.status_code


    def delete_books(self,userId:str,headers:str):
        """
        function:Deleting a user's book list by userId
        :param userId:str
        :param headers:str
        :return:request||MessageModal||status_code
        """
        res = self._session.delete(url=f"{self._url}/BookStore/v1/Books?UserId={userId}",headers=headers)
        if res.status_code == 204:
            return res.request
        if res.status_code == 401:
            return MessageModal(**res.json())
        else:
            return res.status_code

    def get_book(self,isbn:str,headers:str):
        """
        function:Find the book by isbn
        :param isbn:str
        :param headers:str
        :return:BookModal||MessageModal||status_code
        """
        res = self._session.get(url=f"{self._url}/BookStore/v1/Book?ISBN={isbn}",headers=headers)
        book = res.json()
        if res.status_code == 200:
            return BookModal(**book)
        elif res.status_code == 401:
            return MessageModal(**book)
        else:
            return res.status_code

    def delete_book(self,userId:str,headers:str):
        """
        function:deletes the book by userId
        :param stringObject:StringObject
        :param headers:str
        :return:status_code||MessageModal
        """
        res = self._session.delete(url=f"{self._url}/Book{userId}",headers=headers)
        if res.status_code == 200:
            return res.status_code
        elif res.status_code == 401:
            return MessageModal(**res.json())
        else:
            return res.status_code

    def put_books_isbn(self,str_obj_id_isbn:StringObject,isbn:str,headers:str):
        """
        function: Add a book to the user by isbn
        :param str_obj_id_isbn:StringObject
        :param isbn:str
        :param headers:str
        :return:status_code||MessageModal
        """
        res = self._session.put(url=f"{self._url}/BookStore/v1/Books{isbn}", data=str_obj_id_isbn.to_json(),headers=headers)
        if res.status_code == 200:
            return res.status_code
        if res.status_code == 401:
            return MessageModal(**res.json())
        else:
            return res.status_code

    def headers(self,token:str):
        """
        helper function:Returns format of headers
        :param token:str
        :return:str
        """
        headers = {'Authorization': f'Bearer {token}'}
        return headers

