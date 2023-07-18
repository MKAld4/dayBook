from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('search_weather/', views.search_weather, name='search-weather')

]

