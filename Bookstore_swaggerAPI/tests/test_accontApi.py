from Bookstore_swaggerAPI.BookStoreAPI.accontAPI.accountApi import AccontAPI
from Bookstore_swaggerAPI.models.account.login_view_model import LoginViewModel
import pytest


@pytest.fixture()
def accontAPI():
    accontAPI = AccontAPI()
    yield accontAPI


def test_post_accont_authorized(accontAPI):
    user = LoginViewModel(**accontAPI._jsonDB.get_BStore_AccontAPI()["user"])
    message = accontAPI.post_accont_authorized(user)
    assert message == True


def test_post_generateToken(accontAPI):
    user = LoginViewModel(**accontAPI._jsonDB.get_BStore_AccontAPI()["user"])
    token = accontAPI.post_generateToken(user)
    assert token.result == "User authorized successfully."


def test_post_account_user(accontAPI):
    login_view = LoginViewModel(**accontAPI._jsonDB.get_BStore_AccontAPI()["newuser"])
    login_view.new_userName()
    user_result = accontAPI.post_account_user(login_view)
    assert user_result.username == login_view.username


def test_delete_userid(accontAPI):
    user = LoginViewModel(**accontAPI._jsonDB.get_BStore_AccontAPI()["newuser"])
    user.new_userName()
    user_result = accontAPI.post_account_user(user)
    accontAPI.post_accont_authorized(user)
    accontAPI.post_generateToken(user)
    delete = accontAPI.delete_userid(user_result.userId)
    assert delete == 204
    get_user = accontAPI.get_userid(user_result.userId)
    assert get_user.message == "User not found!"


def test_get_userid(accontAPI):
    user = LoginViewModel(**accontAPI._jsonDB.get_BStore_AccontAPI()["newuser"])
    user.new_userName()
    user_result = accontAPI.post_account_user(user)
    accontAPI.post_accont_authorized(user)
    accontAPI.post_generateToken(user)
    get_user = accontAPI.get_userid(user_result.userId)
    assert user_result.userId == get_user.userId
