import pytest
import requests
from helpers import *
from URLS import *


#создание и удаление курьера 
@pytest.fixture
def create_and_delete_courier():
    created_couriers = []

    def _register_and_track():
        courier = create_courier_data()
        payload = {
            "login": courier["login"],
            "password": courier["password"],
            "firstName": courier["first_name"]
        }
        response = requests.post(f"{BASE_URL}{COURIER_CREATE}", data=payload)

        if response.status_code == 201:
            courier["id"] = response.json().get("id")
            courier["creation_response"] = response
            created_couriers.append(courier)
            return courier
        return None

    yield _register_and_track

    for courier in created_couriers:
        if courier and courier.get('id'):
            response = requests.delete(f"{BASE_URL}{COURIER_CREATE}/{courier['id']}")
            if response.status_code != 200:
                print(f"Не удалось удалить курьера с ID {courier['id']}, статус: {response.status_code}")
           
            
            
            
            if response.status_code != 200:
                print(f"Не удалось удалить курьера с ID {courier['id']}, статус: {response.status_code}")