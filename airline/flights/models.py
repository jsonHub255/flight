from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()
    
    def __str__(self):
        return f"{self.id}: {self.origin} To {self.destination} Take {self.duration} min"
    