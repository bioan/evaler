from django.db import models


# Create your models here.

class Participant(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    event = models.ForeignKey('Event', related_name='participants', on_delete=models.CASCADE)


class Event(models.Model):
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
