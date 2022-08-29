from Bookstore_swaggerAPI.BookStoreAPI.accontAPI.accountApi import AccontAPI
from Bookstore_swaggerAPI.BookStoreAPI.storeAPI.storeApi import StoreApi
from Bookstore_swaggerAPI.models.account.login_view_model import LoginViewModel
from Bookstore_swaggerAPI.models.store.add_list_of_books import addListOfBooks
from Bookstore_swaggerAPI.models.store.string_object import StringObject
import pytest

# https://bookstore.toolsqa.com/swagger/
@pytest.fixture()
def token():
    accontAPI = AccontAPI()
    user = LoginViewModel(**accontAPI._jsonDB.get_BStore_Store_Api()["user"])
    token = accontAPI.post_generateToken(user)
    yield token.token


@pytest.fixture()
def accontAPI():
    accontAPI = AccontAPI()
    yield accontAPI


@pytest.fixture()
def storeApi():
    storeApi = StoreApi()
    yield storeApi


def test_get_books(storeApi):
    allbooks = storeApi.get_books()
    assert allbooks.books[0].__module__ == "Bookstore_swaggerAPI.models.store.book_modal"


def test_post_list_books(storeApi, token):
    listbook = addListOfBooks(**storeApi._jsonDB.get_BStore_Store_Api()["listbook"])
    headers = storeApi.headers(token)
    add_list_of_books = storeApi.post_list_books(listbook, headers)
    assert add_list_of_books.isbns[0] == listbook.collectionOfIsbns[0]


def test_delete_books(storeApi, token):
    userId = storeApi._jsonDB.get_BStore_Store_Api()["listbook"]["userId"]
    headers = storeApi.headers(token)
    message = storeApi.delete_books(userId, headers)
    assert str(message) == "<PreparedRequest [DELETE]>"


def test_get_book(storeApi, token):
    isbn = storeApi._jsonDB.get_BStore_Store_Api()["get_book"]["isbn"]
    headers = storeApi.headers(token)
    book = storeApi.get_book(isbn, headers)
    print(book)
    assert book.isbn == isbn


def test_delete_book(storeApi, token):
    userId_isbn = StringObject(**storeApi._jsonDB.get_BStore_Store_Api()["string_object_id&isbn"])
    headers = storeApi.headers(token)
    message = storeApi.delete_book(userId_isbn, headers)
    assert message == 200


def test_put_books_isbn(storeApi, token):
    userId_isbn = StringObject(**storeApi._jsonDB.get_BStore_Store_Api()["string_object_id&isbn"])
    isbn=storeApi._jsonDB.get_BStore_Store_Api()["get_book"]["isbn"]
    headers = storeApi.headers(token)
    code=storeApi.put_books_isbn(userId_isbn,isbn,headers)
    assert code == 200

