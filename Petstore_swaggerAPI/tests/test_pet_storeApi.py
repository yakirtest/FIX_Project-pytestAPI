import pytest
from Petstore_swaggerAPI.PetStoreAPI.storeAPI.storeApi import PetstoreApi
from Petstore_swaggerAPI.models.store.order import Order

#
# @pytest.fixture()
# def order():
#     order = {"id": 5, "petId": 4567, "quantity": 6, "shipDate": "2022-08-06T11:28:12.100+00:00", "status": "approved",
#              "complete": True}
#     yield order


@pytest.fixture()
def pet_storeApi():
    pet_storeApi = PetstoreApi()
    yield pet_storeApi


def test_get_pet_inventory_by_status(pet_storeApi):
    code = pet_storeApi.get_pet_inventory_by_status()
    assert code == 200


def test_post_order_pet(pet_storeApi):
    order = Order(**pet_storeApi._jsonDB.get_PStore_Pet_storeApi()["order"])
    get_order = pet_storeApi.post_order_pet(order)
    assert get_order.id == order.id and get_order.petId == order.petId


def test_get_order_by_orderid(pet_storeApi):
    order = Order(**pet_storeApi._jsonDB.get_PStore_Pet_storeApi()["order"])
    get_order = pet_storeApi.get_order_by_orderid(order.id)
    assert get_order.id == order.id and get_order.petId == order.petId


def test_delete_orderid(pet_storeApi):
    delete_orderid = pet_storeApi._jsonDB.get_PStore_Pet_storeApi()["delete_orderid"]
    code_delete = pet_storeApi.delete_orderid(delete_orderid)
    assert code_delete == 200
    get_code = pet_storeApi.get_order_by_orderid(delete_orderid)
    assert get_code == 404
