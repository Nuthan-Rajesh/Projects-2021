from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    hotel_id = models.IntegerField(default=0)
    customer_need = models.CharField(max_length=150)
    hotel_name = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=13)
    message = models.TextField(blank=True)    
    user_id = models.IntegerField(blank=True)
    create_date = models.DateTimeField(blank=True,default=datetime.now)
    
    def __str__(self):
        return self.email
    