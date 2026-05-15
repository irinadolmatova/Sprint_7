import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


ERROR_NOT_ENOUGH_DATA_CREATE = "Недостаточно данных для создания учетной записи"
ERROR_LOGIN_ALREADY_USED = "Этот логин уже используется"
ERROR_NOT_ENOUGH_DATA_LOGIN = "Недостаточно данных для входа"
ERROR_ACCOUNT_NOT_FOUND = "Учетная запись не найдена"


ORDER_CREATE_DATA = {
    "firstName": "Irina",
    "lastName": "Dolmatova",
    "address": "Addres",
    "metroStation": 3,
    "phone": "+79991112233 ",
    "rentTime": 3,
    "deliveryDate": "2026-12-12",
    "comment": "Comment",
}