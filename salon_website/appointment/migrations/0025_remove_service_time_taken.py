# Generated by Django 3.0.7 on 2020-07-08 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0024_auto_20200708_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='time_taken',
        ),
    ]
