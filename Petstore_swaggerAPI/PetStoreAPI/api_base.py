import requests

from Handling_JSON.read_json_DB_container import Read_the_json_file_DB


class Api_Base:
    # http://localhost:8080/
    def __init__(self, url="http://localhost:8080/api/v3"):
        self._jsonDB = Read_the_json_file_DB()
        self._url = self._jsonDB.get_PStore_Api_Base()["url"]
        self._header = self._jsonDB.get_PStore_Api_Base()["header"]
        self.session = requests.session()
        self.session.headers.update(self._header)
