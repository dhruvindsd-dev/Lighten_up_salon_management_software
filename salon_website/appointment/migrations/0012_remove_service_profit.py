# Generated by Django 3.0.7 on 2020-06-21 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0011_auto_20200621_0332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='profit',
        ),
    ]
