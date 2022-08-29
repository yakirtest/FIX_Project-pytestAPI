from Bookstore_swaggerAPI.BookStoreAPI.api_base import Api_Base
from Bookstore_swaggerAPI.models.account.create_user_result import CreateUserResult
from Bookstore_swaggerAPI.models.account.get_user_result import GetUserResult
from Bookstore_swaggerAPI.models.account.login_view_model import LoginViewModel
from Bookstore_swaggerAPI.models.account.message_modal import MessageModal
from Bookstore_swaggerAPI.models.account.token_view_model import TokenViewModel


class AccontAPI(Api_Base):

    def post_accont_authorized(self,user:LoginViewModel):
        """
        function:Login user
        :param user:LoginViewModel
        :return:bool || MessageModal
        """
        res=self._session.post(f"{self._url}/Account/v1/Authorized",data=user.to_json())
        message=res.json()
        if res.status_code == 200:
            return message
        elif res.status_code==400 or 404:
            return MessageModal(**message)

    def post_generateToken(self,user : LoginViewModel):
        """
        function:generate Token to the user
        :param user:LoginViewModel
        :return: TokenViewModel
        """
        res = self._session.post(f"{self._url}/Account/v1/GenerateToken", data=user.to_json())
        token=res.json()
        if res.status_code == 200:
            token_view_model=TokenViewModel(**token)
            self._headers = {"authorization": f"Bearer {token_view_model.token}"}
            self._session.headers.update(self._headers)
            return token_view_model
        elif res.status_code == 400:
            return MessageModal(**token)
        else:
            return res.status_code

    def post_account_user(self,user : LoginViewModel):
        """
        function: Register a user
        :param user:LoginViewModel
        :return:CreateUserResult ||MessageModal ||status_code
        """
        res = self._session.post(f"{self._url}/Account/v1/User", data=user.to_json(),headers=self._header)
        user = res.json()
        if res.status_code == 201:
            return CreateUserResult(**user)
        elif res.status_code == 404 or 406:
            return MessageModal(**user)
        else:
            return res.status_code

    def delete_userid(self, userId:str):
        """
        function:Delete a user
        :param userId:str
        :return:status_code ||MessageModal
        """
        res = self._session.delete(url=f"{self._url}/Account/v1/User/{userId}",headers=self._headers)
        if res.status_code== 204:
            return res.status_code
        if res.status_code ==200 or 401:
            return MessageModal(**res.json())
        else:
            return res.status_code

    def get_userid(self,userId:str):
        """
        function:Find a user by userId
        :param userId:str
        :return:GetUserResult||MessageModal||status_code
        """
        res = self._session.get(url=f"{self._url}/Account/v1/User/{userId}",headers=self._header)
        user=res.json()
        if res.status_code == 200:
            return GetUserResult(**user)
        elif res.status_code == 401:
            return MessageModal(**user)
        else:
            return res.status_code


