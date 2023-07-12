
import uuid
from django.db import models

from files.models import files


class city(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    

class roomtype(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=100) 
    equipements=models.CharField(max_length=25)



class hotel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    city= models.ManyToManyField(city)
    commodation= models.CharField(max_length=100)
    localisation=models.URLField()
    roomtype=models.ManyToManyField(roomtype)
    price=models.IntegerField()
    files= models.ManyToManyField(files)
    notice=models.CharField(max_length=255)
  
