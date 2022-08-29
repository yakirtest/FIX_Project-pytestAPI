from Petstore_swaggerAPI.PetStoreAPI.userAPI.userApi import UserApi
from Petstore_swaggerAPI.models.user.user import User
import pytest

@pytest.fixture()
def userApi():
    userApi = UserApi()
    yield userApi


def test_post_create_user(userApi):
    user = User(**userApi._jsonDB.get_PStore_User_Api()["newUser"])
    get_user = userApi.post_create_user(user)
    assert get_user.username == user.username and get_user.password == user.password


def test_post_create_with_list_users(userApi):
    listUsers = userApi._jsonDB.get_PStore_User_Api()["listUsers"]
    Users = list(map(lambda user: User(**user), listUsers))
    get_users = userApi.post_create_with_list_users(Users)
    assert get_users[0].username == Users[0].username


def test_get_login_user(userApi):
    name_password = userApi._jsonDB.get_PStore_User_Api()["user_name_password"]
    login = userApi.get_login_user(name_password['username'], name_password['password'])
    assert login[0:23] == "Logged in user session:"


def test_get_logout_user(userApi):
    logout = userApi.get_logout_user()
    assert logout == "User logged out"


def test_get_user_by_username(userApi):
    user = User(**userApi._jsonDB.get_PStore_User_Api()["newUser"])
    get_users = userApi.get_user_by_username(user.username)
    assert get_users.username == user.username and user.id == get_users.id


def test_put_updata_user(userApi):
    user = User(**userApi._jsonDB.get_PStore_User_Api()["newUser"])
    updata_user = userApi._jsonDB.get_PStore_User_Api()["put_updata_user"]
    user.firstName = updata_user["firstName"]
    user.lastName = updata_user["lastName"]
    get_user = userApi.put_updata_user(user.username, user)
    assert get_user.lastName == updata_user["lastName"] and get_user.firstName == updata_user["firstName"]


def test_delete_user(userApi):
    name = userApi._jsonDB.get_PStore_User_Api()["delete_user"]["username"]
    code = userApi.delete_user(name)
    assert code == 200
    user=userApi.get_user_by_username(name)
    assert user == 404

