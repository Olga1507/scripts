import requests

url_list = list()

url_list.append('https://furnitura.ru/')
url_list.append('https://www.r-studio.com')
url_list.append('http://www.uniyar.ac.ru')
url_list.append('https://anderson-yaroslavl.ru')
url_list.append('https://volkovteatr.ru')
url_list.append('https://wordmeter.ru')

# i = 0
response = ''
for url in url_list:
    for i in range(100):
        #print(i)
        response = requests.get(url)
        print(response.status_code)

# response = requests.get(url)
# print(response.status_code)
# print(response.text)
