from Petstore_swaggerAPI.models.pet_store_base import Pet_store_base


class User(Pet_store_base):

    def __init__(self, id: int, username: str, firstName: str, lastName: str, email: str, password: str, phone: str,
                 userStatus: int):
        self._id = id
        self._username = username
        self._firstName = firstName
        self._lastName = lastName
        self._email = email
        self._password = password
        self._phone = phone
        self._userStatus = userStatus

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: list):
        self._id = id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, firstName):
        self._firstName = firstName

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, lastName):
        self._lastName = lastName