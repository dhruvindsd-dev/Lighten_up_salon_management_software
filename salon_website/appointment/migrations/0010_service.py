# Generated by Django 3.0.7 on 2020-06-21 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0009_auto_20200614_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('profit', models.IntegerField()),
                ('catagory', models.CharField(max_length=150)),
            ],
        ),
    ]