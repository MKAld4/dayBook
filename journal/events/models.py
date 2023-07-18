from django.db import models


class Event(models.Model):
    event = models.CharField('What happened', max_length=50, default='')
    message = models.TextField('It was')
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.event

