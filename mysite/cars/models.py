from django.contrib.auth.models import User
from django.db import models

from cars.validators import validate_number_car


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=9, unique=True, validators=[validate_number_car])
    mark = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
