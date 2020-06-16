# Generated by Django 3.0.7 on 2020-06-13 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('confirmation', models.BooleanField(default=False)),
                ('work_done', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Time_slots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_available', models.CharField(max_length=500)),
                ('time_booked', models.CharField(max_length=500)),
            ],
        ),
    ]
