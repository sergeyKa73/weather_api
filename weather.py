from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from  kivy.core.window import Window

from get_datetime import date
from get_quote import quote

import requests
import fake_useragent

# Set the app size
Window.size = (700, 600)

# Designate Uur .kv design file
Builder.load_file('weather.kv')

class MyLayout(Widget):
    def press(self):
        self.ids.name_date.text = f"{date}"
        self.ids.name_quote.text = f"\"{quote['quoteText']}\"\nАвтор: {quote['quoteAuthor']}"
        # Create variables for our widget

        city_name = self.ids.name_input.text

        URL = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&lang=ru&appid=7be386ba1183269a3ef3f47aec09c1c1&units=metric'
        user = fake_useragent.UserAgent().random
        HEADERS = {'user-agent': user}

        def get_html(url, params=''):
            r = requests.get(url, headers=HEADERS, params={'city_name': 'city_name'})
            if r.ok:  # 200
                return r.json()
            print(r.status_code)

        # поиск в словаре по ключу
        def recurs_find_key(key, obj):
            if key in obj:
                return obj[key]
            for k, v in obj.items():
                if type(v) == dict:
                    result = recurs_find_key(key, v)
                    if result is not None:
                        return result
                elif type(v) == list:
                    for i in v:
                        result = recurs_find_key(key, i)
                        if result is not None:
                            return result

        # создаем словарь для введенного города
        def weather_city_dict(obj):
            city_dict = {}
            city_dict.setdefault('country', recurs_find_key('country', obj))
            city_dict.setdefault('city', recurs_find_key('name', obj))
            city_dict.setdefault('t °C', recurs_find_key('temp', obj))
            city_dict.setdefault('wind speed', recurs_find_key('speed', obj))
            city_dict.setdefault('weather', recurs_find_key('description', obj))
            return city_dict

        res = get_html(URL)
        dict_my = weather_city_dict(res)
        my_list = []
        for k, v in dict_my.items():
            my_list.append( f'{k} : {v}')

        x = ''
        for item in my_list:
            x = f'{x} {item}\n'

        # Update thr label
        self.ids.name_label.text = f"{x}"

        # Clear input box
        self.ids.name_input.text = ''


class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()