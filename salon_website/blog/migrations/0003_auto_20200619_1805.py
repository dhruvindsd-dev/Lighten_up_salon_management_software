# Generated by Django 3.0.7 on 2020-06-19 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200618_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='img_link',
            field=models.CharField(blank=True, max_length=550, null=True),
        ),
    ]