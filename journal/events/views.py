from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from events.forms import EventForm
from events.models import Event
from events.serializers import EventSerializer


def events(request):
    return render(request, 'events.html')


class EventsView(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


def create(request):
    form = EventForm()
    data = {
        'form': form
    }
    return render(request, 'events_form.html', data)
