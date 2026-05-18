import pytest
import allure
from data import *
from api_methods.api_client import APIClient

class TestCourierCreation:

    @allure.title('Успешное создание курьера')
    def test_create_courier_success(self, create_courier, delete_courier):
        courier = create_courier()
        assert courier is not None
        response = courier["creation_response"]
        assert response.status_code == 201
        assert response.json() == {"ok": True}
        delete_courier(courier["id"])



    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self, create_courier, delete_courier):
        first_courier = create_courier()
        assert first_courier is not None

        duplicate_payload = {
            "login": first_courier["login"],
            "password": first_courier["password"],
            "firstName": first_courier["first_name"]
        }
        response = APIClient.create_courier(duplicate_payload)
        assert response.status_code == 409
        assert "message" in response.json()
        assert ERROR_LOGIN_ALREADY_USED in response.json()["message"]
        delete_courier(first_courier["id"])
        


    @allure.title("Создание курьера с отсутствующим обязательным полем: {missing_field}")
    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_missing_required_fields(self, missing_field, create_courier, delete_courier):
        courier = create_courier()
        assert courier is not None
        payload = {
            "login": courier["login"],
            "password": courier["password"],
            "firstName": courier["first_name"]
        }
        del payload[missing_field]

        response = APIClient.create_courier(payload)
        assert response.status_code == 400
        assert "message" in response.json()
        assert ERROR_NOT_ENOUGH_DATA_CREATE in response.json()["message"]
        