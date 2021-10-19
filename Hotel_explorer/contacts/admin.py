from django.contrib import admin

from contacts.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','hotel_name','city','create_date')
    list_display_links = ('id','first_name','last_name')
    search_fields = ('first_name','last_name','email','hotel_name')
    list_per_page = 20


admin.site.register(Contact,ContactAdmin)