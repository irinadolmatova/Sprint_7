import pytest
import allure
import requests
from urls import BASE_URL, COURIER_CREATE, COURIER_LOGIN
from helpers import *

class TestCourierLogin:

    @allure.title("Успешная авторизация курьера")
    def test_login_success(self, create_and_delete_courier):
        courier = create_and_delete_courier()
        assert courier is not None

        payload = {
            "login": courier["login"],
            "password": courier["password"],
            "firstName": courier["first_name"]
        }
        response = requests.post(f"{BASE_URL}{COURIER_CREATE}", data=payload)
        assert response.status_code == 200
        user_data = response.json()
        assert "id" in user_data



    @allure.title("Ошибка при неверном логине/пароле: 404")
    @pytest.mark.parametrize("wrong_field", ["wrong_login", "wrong_password"])
    def test_login_with_wrong_credentials(self, wrong_field, create_and_delete_courier):
        courier = create_and_delete_courier()
        assert courier is not None

        if wrong_field == "wrong_login":
            payload = {"login": "wronglogin", "password": courier["password"]}
        else:
            payload = {"login": courier["login"], "password": "wrongpassword"}

        response = requests.post(f"{BASE_URL}{COURIER_LOGIN}", data=payload)
        assert response.status_code == 404
        assert "message" in response.json()
        assert ERROR_ACCOUNT_NOT_FOUND in response.json()["message"]



    @allure.title("Отсутствие обязательных полей login или password возвращает ошибку 400")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_missing_fields(self, missing_field):
        payload = {"login": "testlogin", "password": "testpass"}
        del payload[missing_field]
        response = requests.post(f"{BASE_URL}{COURIER_LOGIN}", data=payload)
        assert response.status_code == 400
        assert "message" in response.json()
        assert ERROR_NOT_ENOUGH_DATA_LOGIN in response.json()["message"]   



    @allure.title("Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку")
    def test_login_nonexistent_user_returns_error(self):
        payload = {
            "login": "nonexistent_login_12345",
            "password": "nonexistent_password_12345"
        }
        response = requests.post(f"{BASE_URL}{COURIER_LOGIN}", data=payload)
        assert response.status_code == 404
        assert "message" in response.json()
        assert ERROR_NOT_ENOUGH_DATA_LOGIN in response.json()["message"]