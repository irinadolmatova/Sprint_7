import pytest
import requests
from helpers import generate_random_string
from urls import BASE_URL, COURIER_CREATE, COURIER_LOGIN

#генерация нового уникального пользователя
@pytest.fixture
def register_new_courier():
    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f"{BASE_URL}{COURIER_CREATE}", data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass 

#получение id курьера
@pytest.fixture
def get_courier_id(register_new_courier):
    if register_new_courier:
        login = register_new_courier["login"]
        password = register_new_courier["password"]

        payload = {"login": login, "password": password}
        response = requests.post(f"{BASE_URL}{COURIER_LOGIN}", data=payload)
        if response.status_code == 200:
            courier_id = response.json().get("id")
            register_new_courier["id"] = courier_id
            return register_new_courier
    return None

#создание и удаление курьера 
@pytest.fixture
def create_and_delete_courier():
    created_couriers = []

    def _register_and_track():
        courier = register_new_courier()
        if courier:
            created_couriers.append(courier)
        return courier

    yield _register_and_track

    for courier in created_couriers:
        if courier and courier['id']:
            response = requests.delete(f"{BASE_URL}{COURIER_CREATE}/{courier['id']}")
            if response.status_code != 200:
                print(f"Не удалось удалить курьера с ID {courier['id']}, статус: {response.status_code}")