from django.contrib import admin

# Register your models here.
from .models import Client, Appointment, Time_slots

admin.site.register(Client)
admin.site.register(Appointment)
admin.site.register(Time_slots)
