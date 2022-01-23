import urllib.request
import requests
import fake_useragent
import json


city_name = input()

URL =f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&lang=ru&appid=7be386ba1183269a3ef3f47aec09c1c1&units=metric'

user = fake_useragent.UserAgent().random
HEADERS= {'user-agent': user}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params={'city_name': 'city_name'})
    print(r.url)
    return r.json()


def get_data(url):
    web_file = urllib.request.urlopen(url)
    if web_file.code == 200:  # 200
        return web_file.read()
    print(web_file.code)

def main():
    res = get_html(URL)
    print(res)
    # print(get_data(URL))

if __name__=='__main__':
    main()