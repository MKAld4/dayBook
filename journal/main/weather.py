import datetime as dt

import requests
from decouple import config

API_KEY = config('API_KEY', default='')

my_weather = {}


def weather(CITY):
    # ? in link to make an opportunity to add smth in the end
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

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
def get_my_weather_json():
    res = weather("Minsk")
    # print(res.json())
    return res.json()


# Dictionary for main page
response = get_my_weather_json()

my_weather = {
    'Temperature': f"{response['main']['temp'] - 273:.2f}C\N{DEGREE SIGN}",
    'Filling': f"{response['main']['feels_like'] - 273:.2f}C\N{DEGREE SIGN}",
    'Humidity': f"{response['main']['humidity']:}%",
    'Wind': f"{response['wind']['speed']:.2f}m/s",
    'Sunrise': f"{dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])}",
    'Sunset': f"{dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])}",
    'Generally': f"{response['weather'][0]['description']}",
}


# for k, v in my_weather.items():
#     print(k+"\t", v)


# Dictionary for search
def get_weather_json(other_city):
    res = weather(other_city)
    if not res.ok:
        print('Oh')
    else:
        response1 = res.json()
        other_weather = {
            'Temperature': f"{response1['main']['temp'] - 273:.2f}C\N{DEGREE SIGN}",
            'Filling': f"{response1['main']['feels_like'] - 273:.2f}C\N{DEGREE SIGN}",
            'Humidity': f"{response1['main']['humidity']:}%",
            'Wind': f"{response1['wind']['speed']:.2f}m/s",
            'Sunrise': f"{dt.datetime.utcfromtimestamp(response1['sys']['sunrise'] + response1['timezone'])}",
            'Sunset': f"{dt.datetime.utcfromtimestamp(response1['sys']['sunset'] + response1['timezone'])}",
            'Generally': f"{response1['weather'][0]['description']}",
        }
        return other_weather

# searched = input('City is ')
# other_city_weather = get_weather_json(searched)
# for k, v in other_city_weather.items():
#     print(k + "\t", v)
