from Petstore_swaggerAPI.models.user.user import User
from Petstore_swaggerAPI.PetStoreAPI.api_base import Api_Base


class UserApi(Api_Base):

    def post_create_user(self, user:User):
        """
        function:Create a user
        :param user:User
        :return: User || status_code
        """
        res = self.session.post(url=f"{self._url}/user",json=user.to_json())
        user_get = res.json()
        if res.status_code == 200:
            return User(**user_get)
        else:
            return res.status_code

    def post_create_with_list_users(self, user_data:list[User]):
        """
        function: Create users with a list
        :param user_data:list[User]
        :return:list[User]
        """
        list_Users = list(map(lambda user: user.to_json(), user_data))
        res = self.session.post(url=f"{self._url}/user/createWithList",json=list_Users)
        users = res.json()
        if res.status_code == 200:
            list_users = list(map(lambda user: User(**user), users))
            return list_users
        else:
            return res.status_code

    def get_login_user(self,username:str,password:int):
        """
        function:User login
        :param username:str
        :param password:int
        :return:text || status_code
        """
        res = self.session.get(url=f"{self._url}/user/login?username={username}&password={password}")
        if res.status_code == 200:
            return res.text
        else:
            return res.status_code

    def get_logout_user(self):
        """
        function:User logout
        :return:text || status_code
        """
        res = self.session.get(url=f"{self._url}/user/logout")
        if res.status_code == 200:
            return res.text
        else:
            return res.status_code

    def get_user_by_username(self,username:str):
        """
        function:Get user by username
        :param username:str
        :return:User
        """
        res = self.session.get(url=f"{self._url}/user/{username}")
        if res.status_code == 200:
            user = res.json()
            return User(**user)
        else:
            return res.status_code

    def put_updata_user(self, username:str,user:User):
        """
        function:Update user information by username
        :param username:str
        :param user:User
        :return:User || status_code
        """
        res = self.session.put(url=f"{self._url}/user/{username}", json=user.to_json())
        user = res.json()
        if res.status_code == 200:
            return User(**user)
        else:
            return res.status_code

    def delete_user(self, username:str):
        """
        function:Deleting a user by username
        :param username:str
        :return:status_code
        """
        res = self.session.delete(url=f"{self._url}/user/{username}")
        if res.status_code == 200:
            return res.status_code
        else:
            return res.status_code

