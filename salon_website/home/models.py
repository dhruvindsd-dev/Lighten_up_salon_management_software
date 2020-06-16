from django.db import models
from appointment.models import Client
# Create your models here.


class Regi_key(models.Model):
    token = models.CharField(max_length=500)
    cli = models.ForeignKey(
        Client, on_delete=models.CASCADE, default=None, null=True)
