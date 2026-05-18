import pytest
import allure
from data import *
from api_methods.api_client import APIClient
from helpers import*

class TestCourierLogin:

    @allure.title("Успешная авторизация курьера")
    def test_login_success(self, create_courier, delete_courier):
        courier = create_courier()
        assert courier is not None

        payload = {
            "login": courier["login"],
            "password": courier["password"]
        }
        response = APIClient.login_courier(payload)
        assert response.status_code == 200
        user_data = response.json()
        assert "id" in user_data
        delete_courier(courier["id"])



    @allure.title("Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку")
    def test_login_nonexistent_user_returns_error(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }
        response = APIClient.login_courier(payload)
        assert response.status_code == 404
        assert "message" in response.json()
        assert ERROR_ACCOUNT_NOT_FOUND in response.json()["message"]



    @allure.title("Отсутствие обязательных полей login или password возвращает ошибку 400")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_missing_fields(self, missing_field):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }
        del payload[missing_field]
        response = APIClient.login_courier(payload)
        assert response.status_code == 400
        assert "message" in response.json()
        assert ERROR_NOT_ENOUGH_DATA_LOGIN in response.json()["message"]   



    
        