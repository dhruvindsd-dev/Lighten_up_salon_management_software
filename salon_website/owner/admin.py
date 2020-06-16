from django.contrib import admin

# Register your models here.
from .models import Owner, Salon_token_ids, Staff

admin.site.register(Owner)
admin.site.register(Salon_token_ids)
admin.site.register(Staff)
