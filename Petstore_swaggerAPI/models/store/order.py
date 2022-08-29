from Petstore_swaggerAPI.models.pet_store_base import Pet_store_base
from Petstore_swaggerAPI.models.store.status import Status


class Order(Pet_store_base):
    def __init__(self, id: int, petId: int, quantity:int, shipDate:str, status:Status, complete:bool):
        self._id=id
        self._petId=petId
        self._quantity=quantity
        self._shipDate=shipDate
        self._status=status
        self._complete=bool(complete)

    @property
    def id(self):
        return self._id


    @property
    def petId(self):
        return self._petId

