# Generated by Django 3.2.8 on 2021-10-14 11:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_alter_hotel_hotel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]