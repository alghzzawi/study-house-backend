from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.IntegerField(null=True, blank=True)
    Is_employee = models.BooleanField(default=False, blank=True)