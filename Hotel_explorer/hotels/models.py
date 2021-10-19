from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from multiselectfield import MultiSelectField

# Create your models here

    
class Hotel(models.Model):

    amenity_choices = (
        	('Beach View','Beach View'),
            ('Laundry service','Laundry service'),
            ('Salon','Salon'),
            ('Spa','Spa'),
            ('Restaurant','Restaurant'),
            ('Hot bath','Hot bath'),
            ('Nightclub / DJ','Nightclub / DJ'),
            ('Entertainment staff','Entertainment staff'),
            ('Bar / lounge','Bar / lounge'),
            ('Fitness Centre with Gym / Workout Room','Fitness Centre with Gym / Workout Room'),
            ('Pool','Pool'),
            ('Free High Speed Internet (WiFi)','Free High Speed Internet (WiFi)'),
            ('Free Parking','Free Parking'),
            ('AC','Air Conditioner'),
    )
    city_choice = (
        ('HYD','Hyderabad'),
        ('MHA','Mahabalipuram'),
        ('VAD','Vadodara')
    )

    hotel_name = models.CharField(max_length=100)
    hotel_description = RichTextField()
    price = models.IntegerField()
    city = models.CharField(choices = city_choice,max_length=100)
    address = models.CharField(max_length=200)
    hotel_photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    hotel_photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    hotel_photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    hotel_photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    hotel_photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    amenities = MultiSelectField(choices = amenity_choices,max_length=200)
    created_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.hotel_name