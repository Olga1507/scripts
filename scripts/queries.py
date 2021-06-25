"""
 В этом файле содержатся фу-ии, которые проверяют (логин, пароль),
 совершая запрос к сайту

 def func(login, password) -> bool:
    ...
"""
import time

import requests


def request_local_server(login, password):
    response = requests.post(
        'http://127.0.0.1:5000/auth',
        json={'login': login, 'password': password}
    )
    # return response.status_code == 200 (краткая версия кода ниже)
    if response.status_code == 200:
        return True
    else:
        return False


# Функция для защищенного сервера (применятеся в случае использования nginx)

def request_local_server_protected(login, password):
    attempts = 3
    for i in range(attempts):
        try:
            response = requests.post(
                'http://127.0.0.1:4000/auth',
                json={'login': login, 'password': password}
            )
            if response.status_code == 200:
                return True
        except:
            pass

        if i + 1 < attempts:
            time.sleep(1)

        # if response.status_code != 200:
        #     # TODO повторить


# Функция для запросов на "абстрактный сайт"

def request_some_site(login, password):
    response = requests.put(
        'https://example.com/login',
        headers={'Host': 'example.com'},
        data={'login': login, 'password': password}
    )
    return response.status_code == 200

# JSON: {"login": "admin", "password": "12345"}
# form-data: login=admin&password=12345
