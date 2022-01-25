# получения цитат
import requests
import fake_useragent


URL='http://api.forismatic.com/api/1.0/'
user = fake_useragent.UserAgent().random
HEADERS= {'user-agent': user}


def get_quote(url, params=''):
    r = requests.get(url, headers=HEADERS, params={'method':'getQuote', 'key': 457653,'format':'json', 'lang':'ru'})
    if r.ok:  # 200
        return r.json()
    print(r.status_code)


quote = (get_quote(URL))

if __name__ == '__main__':
    print(get_quote(URL))