# Generated by Django 3.2.8 on 2021-10-14 11:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hotel_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
