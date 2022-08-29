from Petstore_swaggerAPI.models.store.order import Order
from Petstore_swaggerAPI.PetStoreAPI.api_base import Api_Base

#http://localhost:8080/
class PetstoreApi(Api_Base):

    def get_pet_inventory_by_status(self):
        """
        function:Returns a map of status codes to quantities
        :return: status_code
        """
        res = self.session.get(url=f"{self._url}/store/inventory")
        if res.status_code == 200:
            return res.status_code
        else:
            return res.status_code

    def post_order_pet(self, order:Order):
        """
        function:Place an order for a pet
        :param order:
        :return: Order||status_code
        """
        res = self.session.post(url=f"{self._url}/store/order",json=order.to_json())
        order_get = res.json()
        if res.status_code == 200:
            return Order(**order_get)
        else:
            return res.status_code

    def get_order_by_orderid(self,orderid : int):
        """
         function:Find purchase order by ID
        :param orderid: int
        :return:  Order||status_code
        """
        res = self.session.get(url=f"{self._url}/store/order/{orderid}")
        if res.status_code == 200:
            order=res.json()
            return Order(**order)
        else:
            return res.status_code

    def delete_orderid(self, orderid:int):
        """
        function:Delete purchase order by ID
        :param orderid: int
        :return: status_codeה
        """
        res = self.session.delete(url=f"{self._url}/store/order/{orderid}")
        if res.status_code == 200:
            return res.status_code
        else:
            return res.status_code

