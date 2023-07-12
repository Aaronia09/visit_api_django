import uuid
from django.db import models
from hotel.models import city, hotel
from program.models import program
from service.models import service


class pack(models.Model):
    TYPE_CHOICES = [
        ('simple', 'Simple'),
        ('personalisée', 'Personalisée'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    duration = models.CharField(max_length=100)
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    cities = models.ManyToManyField(city)
    services = models.ManyToManyField(service)
    programs=models.ManyToManyField(program)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    hotels = models.ManyToManyField(hotel)
    notice = models.CharField(max_length=255)

