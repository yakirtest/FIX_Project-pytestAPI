from Petstore_swaggerAPI.PetStoreAPI.petAPI.petApi import PetApi
from Petstore_swaggerAPI.models.pat.pet import Pet
import pytest


@pytest.fixture()
def petApi():
    petApi = PetApi()
    yield petApi


def test_post_add_new_pet(petApi):
    turtle = Pet(**petApi._jsonDB.get_PStore_Pet_Api()["Turtle"])
    pet = petApi.post_add_new_pet(turtle)
    assert pet.to_json() == turtle.to_json()


def test_put_updata_pet(petApi):
    rabbit = Pet(**petApi._jsonDB.get_PStore_Pet_Api()["Rabbit"])
    rabbit = petApi.post_add_new_pet(rabbit)
    rabbit.photoUrls = petApi._jsonDB.get_PStore_Pet_Api()["put_updata_pet"]["photoUrls"]
    pet = petApi.put_updata_pet(rabbit)
    assert pet.photoUrls == rabbit.photoUrls

def test_get_pet_by_status(petApi):
    status = petApi._jsonDB.get_PStore_Pet_Api()["Status"]["sold"]
    status_pets = petApi.get_pet_by_status(status)
    assert status_pets[0].status == status


def Equals_tags(tags_pets, tags):
    testing_tag = tags[0]
    for pet in tags_pets:
        for name in range(len(pet.tags)):
            if pet.tags[name]["name"] == testing_tag:
                return True
    return False


def test_get_pet_by_tags(petApi):
    tags = petApi._jsonDB.get_PStore_Pet_Api()["get_pet_by_tags"]["tags"]
    tags_pets = petApi.get_pet_by_tags(tags)
    booltest = Equals_tags(tags_pets, tags)
    assert booltest == True

def test_get_pet_by_id(petApi):
    turtle = Pet(**petApi._jsonDB.get_PStore_Pet_Api()["Turtle"])
    pet = petApi.get_pet_by_id(turtle.id)
    assert pet.id == turtle.id and turtle.name == pet.name

def test_post_update_name_status_pet(petApi):
    update = petApi._jsonDB.get_PStore_Pet_Api()["post_update_name_status_pet"]
    pet = petApi.post_update_name_status_pet(update["id"], update["name"], update["status"])
    assert pet.id == update["id"] and pet.name == update["name"] and pet.status == update["status"]

def test_delete_pet(petApi):
    id = petApi._jsonDB.get_PStore_Pet_Api()["delete_pet"]
    test_pet = petApi.delete_pet(id)
    assert test_pet == "Pet deleted"
    pet = petApi.get_pet_by_id(id)
    assert pet == "Pet not found"

def test_post_uploadImage_pet(petApi):
    uploadImage = petApi._jsonDB.get_PStore_Pet_Api()["post_uploadImage_pet"]
    upload = petApi.post_uploadImage_pet(uploadImage["photoUrls"], uploadImage["path"], uploadImage["userid"])
    assert upload["code"] == 415 and upload["message"] == "HTTP 415 Unsupported Media Type"
