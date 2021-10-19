from django.contrib import admin
from django.utils.html import format_html
from hotels.models import  Hotel

class HotelAdmin(admin.ModelAdmin):
    
    def thumbnail(self,object):
        return format_html('<img src="{}" width="75" height="75" style="border-radius: 50px;"/>'.format(object.hotel_photo.url))

    list_display = ('id','thumbnail','hotel_name','price')
    list_display_links = ('id','thumbnail','hotel_name')
    search_fields = ('id','hotel_name')


admin.site.register(Hotel,HotelAdmin)