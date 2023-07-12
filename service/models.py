import uuid
from django.db import models




class accessibilities(models.Model):
    name = models.CharField(max_length=255)




class service(models.Model):
    SERVICES_CHOICES=[
    ('activity', 'Activity'),
    ('event', 'Event'),
   
]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    category_service= models.CharField(max_length=50)
    duration = models.DurationField()
    description=models.TextField()
    service_type=models.CharField(max_length=255,choices=SERVICES_CHOICES)
    price=models.IntegerField()
    images= models.ImageField(upload_to='images/')
    notice=models.CharField(max_length=255)
    
