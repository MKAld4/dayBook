from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('create/', views.create, name='create'),
    path('<int:pk>/update', views.EventUpdateView.as_view(), name='event-update'),
    path('<int:pk>/delete', views.EventsDeleteView.as_view(), name='event-delete')

]
