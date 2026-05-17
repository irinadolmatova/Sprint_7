import pytest
import allure
import requests
from URLS import *
from helpers import *

class TestOrderCreation:

    @allure.title("Создание заказа с различными параметрами цвета")
    @pytest.mark.parametrize("colors",[
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            None
        ])
    def test_create_order_with_colors_parametrized(self, colors):
        payload = ORDER_CREATE_DATA.copy()
        if colors is not None:
            payload["color"] = colors
        else:
            payload.pop("color", None)
        response = requests.post(f"{BASE_URL}{ORDERS_LIST}", data=payload)
        assert response.status_code == 201
        assert "track" in response.json()
        