from threading import Thread
import requests

url_list = list()

url_list.append('https://furnitura.ru/')
url_list.append('https://www.r-studio.com')
url_list.append('http://www.uniyar.ac.ru')
url_list.append('https://anderson-yaroslavl.ru')
url_list.append('https://volkovteatr.ru')
url_list.append('https://wordmeter.ru')


def test_url(url_param):
    url_param = str(url_param)
    response = requests.get(url_param)
    # if response.status_code != 200:
    print(url_param + " " + str(response.status_code))


thr_list = list()
print("Running...")
for url in url_list:
    for i in range(100):
        thr = Thread(target=test_url, args=(url,))
        thr_list.append(thr)
        thr.start()
        # test_url(url)
print("END!")
