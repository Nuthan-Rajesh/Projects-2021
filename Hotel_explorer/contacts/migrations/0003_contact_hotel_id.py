# Generated by Django 3.2.8 on 2021-10-18 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_rename_first_naame_contact_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='hotel_id',
            field=models.IntegerField(default=0),
        ),
    ]
