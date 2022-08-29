from Petstore_swaggerAPI.models.pet_store_base import Pet_store_base


class Tag(Pet_store_base):

    def __init__(self, id, name):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name






