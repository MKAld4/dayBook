from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from events.models import Event
from events.serializers import EventSerializer


def events(request):
    return render(request, 'events.html')


class EventsView(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


def create(request):
    return render(request, 'events_form.html')
