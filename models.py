from django.db import models

class Event(models.Model):
    name = models.TextField()
    college  = models.TextField()
    email = models.TextField()
    phone = models.IntegerField()
    date = models.DateField()
    lat = models.FloatField()
    lon = models.FloatField()
    event = models.TextField()
    duration = models.TextField()
    
class User(models.Model):
    username = models.TextField()
    password = models.TextField()
