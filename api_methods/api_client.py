import requests
import allure
from url import URL

class APIClient:

    @staticmethod
    @allure.step('Создание курьера')
    def create_courier(body):
        return requests.post(url=URL.COURIER_CREATE, json=body)
    
    @staticmethod
    @allure.step('Логирование курьера')
    def login_courier(body):
        return requests.post(url=URL.COURIER_LOGIN, json=body)
    
    @staticmethod
    @allure.step('Удаление курьера')
    def delete_courier(courier_id):
        return requests.delete(url=f"{URL.COURIER_CREATE}/{courier_id}")
    
    @staticmethod
    @allure.step('Создание заказа')
    def create_order(body):
        return requests.post(url=URL.ORDERS_CREATE, json=body)
    
    @staticmethod
    @allure.step('Получение списка заказов')
    def get_list_order():
        return requests.get(url=URL.ORDERS_LIST)
    
    