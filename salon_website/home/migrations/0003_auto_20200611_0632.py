# Generated by Django 3.0.7 on 2020-06-11 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200611_0422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regi_key',
            name='active',
        ),
        migrations.RemoveField(
            model_name='regi_key',
            name='interaction_num',
        ),
        migrations.RemoveField(
            model_name='regi_key',
            name='time_counter',
        ),
        migrations.AddField(
            model_name='regi_key',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.User'),
        ),
    ]
