from django.db import models
from .gamer import Gamer


class Event(models.Model):

    organizer = models.ForeignKey(
        "Gamer", on_delete=models.CASCADE, related_name='organized_events')
    description = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    attendees = models.ManyToManyField(Gamer, related_name="events")
