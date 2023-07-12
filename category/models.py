import uuid
from django.db import models

class category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    images= models.ImageField(upload_to='images/')
