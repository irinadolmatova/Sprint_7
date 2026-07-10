import allure
from api_methods.api_client import APIClient

class TestOrdersList:

    @allure.title("Получение списка всех заказов: тело ответа содержит список orders")
    def test_get_orders_list(self):
        response = APIClient.get_list_order()
        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
        