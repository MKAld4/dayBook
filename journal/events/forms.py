from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput
from .models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event', 'message', 'date']

        widgets = {
            'event': TextInput(attrs={'class': 'form-control', 'placeholder': 'What it was?'}),
            'message':  TextInput(attrs={'class': 'form-control', 'placeholder': 'How it was?'}),
            'date': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),)
            # 'date': DateTimeInput(attrs={'class': 'form-control'})
        }
