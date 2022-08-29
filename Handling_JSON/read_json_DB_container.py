import json

class Read_the_json_file_DB:
    def __init__(self):
        with open("C:\Git_sela\FIX_Project-pytestAPI\Handling_JSON\DB_container.json") as file:
            self.data = json.load(file)

    def get_PStore_Api_Base(self):
        return self.data["Pet_Store"]["Api_Base"]

    def get_PStore_Pet_Api(self):
        return self.data["Pet_Store"]["Pet_Api"]

    def get_PStore_Pet_storeApi(self):
        return self.data["Pet_Store"]['Pet_storeApi']

    def get_PStore_User_Api(self):
        return self.data["Pet_Store"]["User_Api"]

    def get_BStore_Api_Base(self):
        return self.data["Book_StoreApi"]["Api_Base"]

    def get_BStore_AccontAPI(self):
        return self.data["Book_StoreApi"]["AccontAPI"]

    def get_BStore_Store_Api(self):
        return self.data["Book_StoreApi"]["Store_Api"]


if __name__ == '__main__':
    json=Read_the_json_file_DB()
    print(json.get_PStore_Api_Base())
    print(json.get_PStore_Pet_Api())
    print(json.get_PStore_Pet_storeApi())
    print(json.get_PStore_User_Api())
    print(json.get_BStore_Api_Base())
    print(json.get_BStore_AccontAPI())
    print(json.get_BStore_Store_Api())



    # with open("C:\Git_sela\pythonProject2\HW_selenium\DB_container.json") as f:
    #     data = json.load(f)
    # print(data['user_name']["valid_user"])
    # print(data['Aut_page_locators']["login_locators"])
    # print(data['Search_page_locators'])
    # print(data['Cart_page_locators'])
    # print(data['Pay_page_locators'])
