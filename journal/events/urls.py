from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('create/', views.create, name='create'),
    # path('<int:pk>', )

]
