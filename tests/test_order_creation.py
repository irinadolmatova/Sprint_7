import pytest
import allure
from generators import create_order_data
from api_methods.api_client import APIClient

class TestOrderCreation:

    @allure.title("Создание заказа с различными параметрами цвета")
    @pytest.mark.parametrize("colors",[
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            None
        ])
    def test_create_order_with_colors_parametrized(self, colors):
        payload = create_order_data(colors)
        response = APIClient.create_order(payload)
        assert response.status_code == 201
        assert "track" in response.json()
        