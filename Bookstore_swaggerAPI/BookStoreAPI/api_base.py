
import requests

from Handling_JSON.read_json_DB_container import Read_the_json_file_DB


class Api_Base:
    # https://bookstore.toolsqa.com
    def __init__(self, url='https://bookstore.toolsqa.com'):
        self._jsonDB = Read_the_json_file_DB()
        self._url = self._jsonDB.get_PStore_Api_Base()["url"]
        self._header = self._jsonDB.get_PStore_Api_Base()["header"]
        self._header = {'accept': 'application/json'}
        self._url = url
        self._session = requests.session()
        self._session.headers.update(self._header)



