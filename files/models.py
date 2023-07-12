import uuid
from django.db import models

class files(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    images= models.ImageField(upload_to='images/')
