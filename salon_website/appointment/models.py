from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=150)
    number = models.IntegerField()


class Appointment(models.Model):
    time = models.TimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True, default=None)
    date = models.DateField(
        auto_now=False, auto_now_add=False, default=None, null=True, blank=True)
    confirmation = models.BooleanField(default=False, null=True)
    work_to_be_done = models.CharField(max_length=500, null=True)
    cli = models.ForeignKey(
        Client, on_delete=models.CASCADE, null=True, default=None)


class Time_slots(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False, default=None)
    time_available = models.CharField(max_length=500)
    time_booked = models.CharField(
        max_length=500, null=True, default=None, blank=True)
# 11:30,12:00,12:30,1:00,1:30,2:00,2:30,3:00,3:30,4:00,4:30,5:00,5:30,6:00,6:30,7:00,7:30
