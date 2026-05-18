import pytest
import logging
from generators import create_courier_data
from api_methods.api_client import APIClient

logger = logging.getLogger(__name__)

#Создание курьера
@pytest.fixture
def create_courier():
    def _create():
        courier_data = create_courier_data()
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"],
            "firstName": courier_data["first_name"]
        }
        response = APIClient.create_courier(payload)

        if response.status_code == 201:
            courier_data["id"] = response.json().get("id")
            courier_data["creation_response"] = response
            return courier_data
        return None

    return _create


#Удаление курьера
@pytest.fixture
def delete_courier():
    def _delete(courier_id):
        response = APIClient.delete_courier(courier_id)
        if response.status_code != 200:
            logger.warning(
                f"Не удалось удалить курьера с ID {courier_id}, статус: {response.status_code}"
            )
    return _delete

