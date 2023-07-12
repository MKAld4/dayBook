import datetime as dt

import requests
# !!!!!!!!!!! Hide keys
# from journal.settings import API_KEY
from decouple import config

API_KEY = config('API_KEY', default='')

my_weather = {}


def weather(CITY):
    # ? in link to make an opportunity to add smth in the end
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    # Use KEY had value written in setting.py or new venv, for the weather.py only can use:
    # API_KEY = open('api_key', 'r').read()
    # Also can just put key
    # API_KEY = ''

    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

    r = requests.get(url)

    if r.status_code == 404:
        print('Error city')
    if not r.ok:
        print("Check status")
    # print(r.status_code)
    # print(r.ok)
    return r


# res = requests.get(url).json()
def get_weather_json():
    res = weather("Minsk")
    # print(res.json())
    return res.json()


response = get_weather_json()

my_weather = {
    'temperature': f"{response['main']['temp'] - 273:.2f}C\N{DEGREE SIGN}",
    'filling': f"{response['main']['feels_like'] - 273:.2f}C\N{DEGREE SIGN}",
    'humidity': f"{response['main']['humidity']:}%",
    'wind': f"{response['wind']['speed']:.2f}m/s",
    'sunrise': f"{dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])}",
    'sunset': f"{dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])}",
    'generally': f"{response['weather'][0]['description']}",
}

# for k, v in my_weather.items():
#     print(k+"\t", v)
