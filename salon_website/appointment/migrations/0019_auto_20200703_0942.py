# Generated by Django 3.0.7 on 2020-07-03 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0018_remove_appointment_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='cli',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='appointment.Client'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='confirmation',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='work_to_be_done',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
