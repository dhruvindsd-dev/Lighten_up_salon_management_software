from django.contrib import admin

# Register your models here.
from .models import Client, Appointment, TimeSlots, Service

admin.site.register(Client)
admin.site.register(Appointment)
admin.site.register(TimeSlots)
admin.site.register(Service)
