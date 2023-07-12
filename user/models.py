import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class user(AbstractUser):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('superadmin', 'Superadmin'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    birthdate = models.DateField()
    sexe = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=True)
