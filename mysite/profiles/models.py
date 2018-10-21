from django.contrib.auth.models import User
from django.db import models


class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    invoice_num = models.IntegerField()