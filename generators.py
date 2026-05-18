from helpers import *
from data import ORDER_DATA

#Создние данных нового курьера без отправки запроса
def create_courier_data():
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "first_name": generate_random_string(10)
    }


def create_order_data(colors):
    payload = ORDER_DATA.copy()
    if colors is None:
        return payload
    payload["color"] = colors
    return payload