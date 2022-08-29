from Petstore_swaggerAPI.models.pat.pet import Pet
from Petstore_swaggerAPI.PetStoreAPI.api_base import Api_Base


# http://localhost:8080/
class PetApi(Api_Base):

    def put_updata_pet(self, pet:Pet):
        """
        function:Update an existing pet by Id
        :param pet:Pet
        :return:Pet
        """
        res = self.session.put(url=f"{self._url}/pet", json=pet.to_json(),headers=self._header)
        pet = res.json()
        if res.status_code == 200:
            my_pet = Pet(**pet)
            return my_pet
        else:
            return res.status_code

    def post_add_new_pet(self, pet: Pet):
        """
        function:Add a new pet to the store
        :param pet:Pet
        :return:Pet||status_code
        """
        res = self.session.post(url=f"{self._url}/pet", json=pet.to_json(),headers=self._header)
        pet_dict = res.json()
        if res.status_code == 200:
            my_pet = Pet(**pet_dict)
            return my_pet
        else:
            return res.status_code

    def get_pet_by_status(self, status: str):
        """
        function:Find all the animals by status:available, pending, sold
        :param status:
        :return:list[Pet]
        """
        res = self.session.get(url=f"{self._url}/pet/findByStatus?status={status}",headers=self._header)
        status_pets = res.json()
        if res.status_code == 200:
            list_pets = list(map(lambda pet: Pet(**pet), status_pets))
            return list_pets
        else:
            return res.status_code

    def get_pet_by_tags(self, tags: [str]):
        """
        function:Finds all Pets by list tags
        :param tags:list[str]
        :return:list[Pet]
        """
        f_tags=self.format_tags(tags)
        res = self.session.get(url=f"{self._url}/pet/findByTags?{f_tags}",headers=self._header)
        tags_pets = res.json()
        list_pets = list(map(lambda pet: Pet(**pet), tags_pets))
        if res.status_code == 200:
            return list_pets
        else:
            return res.status_code

    def format_tags(self,tags):
        """
        helper function: to "get_pet_by_tags"
        function:Returns a tag format
        :param tags:tags:list[str]
        :return:str
        """
        f_tags = ""
        for i in range(len(tags)):
            if len(tags) == 1 or i == len(tags) - 1:
                f_tags += f"tags={tags[i]}"
            else:
                f_tags += f"tags={tags[i]}&"
        return f_tags



    def get_pet_by_id(self, pet_id: int) -> Pet:
        """
        function:Find pet by ID
        :param pet_id:int
        :return:Pet ||text
        """
        res = self.session.get(url=f"{self._url}/pet/{pet_id}",headers=self._header)
        if res.status_code == 200:
            pet = res.json()
            my_pet = Pet(**pet)
            return my_pet
        else:
            return res.text

    def post_update_name_status_pet(self, id: int, name: str, status: str):
        """
        function:Updates a pet in the store with form data
        :param id:int
        :param name:str
        :param status:str
        :return:Pet||status_code
        """
        res = self.session.post(url=f"{self._url}/pet/{id}?name={name}&status={status}",headers=self._header)
        if res.status_code == 200:
            pet = res.json()
            my_pet = Pet(**pet)
            return my_pet
        else:
            return res.status_code

    def delete_pet(self, id: int):
        """
        function:Deletes a pet
        :param id:int
        :return:text || status_code
        """
        res = self.session.delete(url=f"{self._url}/pet/{id}",headers=self._header)
        if res.status_code == 200:
            return res.text
        else:
            return res.status_code

    def post_uploadImage_pet(self, photoUrls:str,path:str,userid:str):
        """
        function:uploads an image
        :param photoUrls:str
        :param path:str
        :param userid:str
        :return:status_code||json
        """
        file = {f"{photoUrls}": (open(f"{path}", 'rb'))}
        res = self.session.post(url=f"{self._url}/pet/{userid}/uploadImage?additionalMetadata=", data=file,headers=self._header)
        if res.status_code == 415:
            return res.json()
        else:
            return res.status_code


