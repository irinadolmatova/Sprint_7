import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

#Создние данных нового курьера без отправки запроса
def create_courier_data():
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "first_name": generate_random_string(10)
    }


ERROR_NOT_ENOUGH_DATA_CREATE = "Недостаточно данных для создания учетной записи"
ERROR_LOGIN_ALREADY_USED = "Этот логин уже используется"
ERROR_NOT_ENOUGH_DATA_LOGIN = "Недостаточно данных для входа"
ERROR_ACCOUNT_NOT_FOUND = "Учетная запись не найдена"


ORDER_CREATE_DATA = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha"
}