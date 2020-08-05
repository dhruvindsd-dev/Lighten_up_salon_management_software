from django.db import models
from appointment.models import Client, Service
# Create your models here.


class Sale_services(models.Model):
    cli = models.ForeignKey(
        Client, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    services = models.CharField(max_length=10000)
    true_price = models.IntegerField(default=None)
    discount = models.IntegerField(default=None, null=True, blank=True)
