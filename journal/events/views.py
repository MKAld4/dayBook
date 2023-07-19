from django.shortcuts import render, redirect
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
    error = ''
    # Get data from form, post - data take from form
    if request.method == 'POST':
        form = EventForm(request.POST)
        # If data correct - save it in table
        if form.is_valid():
            form.save()
            # Return on News page if success
            # Import redirect for this
            return redirect('home')
        else:
            error = 'Wrong form'
    # Make obj on that bases on the class
    form = EventForm()
    # Dictionary
    data = {
        # Give in create.html by the key
        'form': form,
        'error': error
    }

    return render(request, 'events_form.html', data)
