from django.db import models
from utils.models import BaseModel
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customer(AbstractUser):
    address = models.CharField(max_length=100, blank=True, null=True)