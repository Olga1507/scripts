import json

from flask import Flask, request, Response

app = Flask(__name__)

stats = {
    'attempts': 0,
    'success': 0,
}


# создание страницы сервера
@app.route('/')
def hello():
    return f'Hello, Hacker! stats={stats}'


# создание логина/пароля
@app.route('/auth', methods=['POST'])
def auth():
    stats['attempts'] += 1

    data = request.json
    login = data['login']
    password = data['password']
    print(login, password)

    with open('users.json') as users_file:
        users = json.load(users_file)

    if login in users and users[login] == password:
        status_code = 200
        stats['success'] += 1
    else:
        status_code = 401

    return Response(status=status_code)


if __name__ == '__main__':
    app.run()
