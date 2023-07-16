from django.shortcuts import render

from main.weather import my_weather, get_weather_json

# For displaying dictionary
from django.template.defaulttags import register


# Main weather page
def index(request):
    return render(request, 'index.html', {'my_weather': my_weather})


# Substitute for router?


# Searching
def search_weather(request):
    if request.method == "POST":
        searched = request.POST['searched']
        # Variable to display weather
        weather_in = get_weather_json(searched)
        # Check if dictionary empty
        if weather_in:
            return render(request, 'search_weather.html', {'searched': searched, 'weather_in': weather_in})
        else:
            return render(request, 'search_weather.html', {})
    else:
        return render(request, 'search_weather.html', {})
