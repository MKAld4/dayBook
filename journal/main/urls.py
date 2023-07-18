from django.urls import path

from django.conf import settings


urlpatterns = [
    path('', main.views.index, name='home'),
    path('search_weather', main.views.search_weather, name='search-weather')

]

