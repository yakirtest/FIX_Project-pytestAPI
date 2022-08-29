from Petstore_swaggerAPI.models.pat.category import Category
from Petstore_swaggerAPI.models.pat.status import Status
from Petstore_swaggerAPI.models.pet_store_base import Pet_store_base
from Petstore_swaggerAPI.models.pat.tag import Tag

data = {'id': 111, 'name': 'Rabbit1', 'category': {'id': 4567, 'name': 'Rabbits'}, 'photoUrls': ['url1', 'url2'],
        'tags': [{'id': 1, 'name': 'tag3'}, {'id': 2, 'name': 'tag4'}], 'status': 'available'}

data2 = {'id': 111, 'name': 'Rabbit 1', 'category': {'id': 4567, 'name': 'Rabbits'}, 'photoUrls': ['url1', 'url2'],
         'tags': [{'id': 1, 'name': 'tag3'}, {'id': 2, 'name': 'tag4'}], 'status': 'available'}


class Pet(Pet_store_base):

    def __init__(self, id: int, name: str, category: Category, photoUrls: list, tags: Tag, status: Status):
        self._id = id
        self._name = name
        self._category = category
        self._photoUrls = photoUrls
        self._tags = tags
        self._status = status

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name


    @property
    def photoUrls(self):
        return self._photoUrls

    @photoUrls.setter
    def photoUrls(self, photourls: list):
        self._photoUrls = photourls

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status: list):
        self._status = status

    @property
    def tags(self):
        return self._tags

    # @property
    # def name(self):
    #     return self._name

    # if photoUrls is not None:
    #     self.photoUrls = photoUrls
    # if tags is not None:
    #     self.tags = tags
    # if status is not None:
    #     self.status = status

    # def __str__(self):
    #     return f"id:{self.id}\nname:{self.name}\ncategory:{self.category}\nphoto_urls:{self.photoUrls}\ntags:{self.tags}\nstatus:{self.status}"
    #
