# Generated by Django 3.0.7 on 2020-07-05 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_auto_20200624_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale_services',
            name='date',
            field=models.DateField(),
        ),
    ]
