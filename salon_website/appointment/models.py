from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=150)
    number = models.IntegerField()
    anniversery = models.DateField(default=None, null=True, blank=True)
    date_of_birth = models.DateField(
        default=None, null=True, blank=True)


class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    confirmation = models.BooleanField(default=False, null=True)
    work_to_be_done = models.CharField(max_length=500, null=True)
    cli = models.ForeignKey(
        Client, on_delete=models.CASCADE, null=True, default=None)


class TimeSlots(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False, default=None)
    time_available = models.CharField(max_length=500)
    time_booked = models.CharField(
        max_length=500, null=True, default=None, blank=True)
# '11:30', '12:00', '12:30', '01:00', '01:30', '02:00', '02:30', '03:00',
    # '03:30', '04:00', '04:30', '05:00', '05:30', '06:00', '06:30', '07:00', '07:30'


class Service(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    catagory = models.CharField(max_length=150)
    # time_taken = models.IntegerField(null=True)
