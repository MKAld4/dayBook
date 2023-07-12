from django.shortcuts import render

from main.weather import my_weather

# For displaying dictionary
from django.template.defaulttags import register

# Main weather page
def index(request):
    return render(request, 'index.html', {'my_weather': my_weather})


# Substitute for router?
def events(request):
    return render(request, 'events.html')


# Searching
def search_weather(request):
    return render(request, 'search_weather.html', {})

# Searching
# @register.filter
# def get_weather_dict(my_weather, key):
#     return my_weather.get(key)
