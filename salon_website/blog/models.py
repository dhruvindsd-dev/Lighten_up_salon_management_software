from django.db import models

# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to=None, height_field=None,
                            width_field=None, max_length=None, null=True, blank=True)
    img_link = models.CharField(max_length=550, null=True, blank=True)
