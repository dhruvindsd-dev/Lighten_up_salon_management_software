from django.db import models

# Create your models here.


class Owner(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=90)


class Staff(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=90)


class Salon_token_ids(models.Model):
    token = models.CharField(max_length=500)
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, default=None, null=True, blank=True)
    admin = models.ForeignKey(
        Owner, on_delete=models.CASCADE, default=None, null=True, blank=True)
