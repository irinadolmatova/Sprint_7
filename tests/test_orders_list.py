import allure
import requests
from urls import BASE_URL, ORDERS_LIST
from helpers import *

class TestOrdersList:

    @allure.title("Получение списка всех заказов: тело ответа содержит список orders")
    def test_get_orders_list(self):
        response = requests.get(f"{BASE_URL}{ORDERS_LIST}")
        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json(), list)