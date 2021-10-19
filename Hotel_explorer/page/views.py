from django.shortcuts import render,redirect
from hotels.models import  Hotel
from django.contrib import messages


# Create your views here.

def home(request):
    all_hotels = Hotel.objects.order_by('-created_date')
    city_search = Hotel.objects.values_list('city',flat=True).distinct()
    data = {
        'all_hotels':all_hotels,
        'city_search':city_search,
    }
    return render(request,'page/home.html',data)

def about(request):
    return render(request,'page/about.html')

def contact(request):
    if request.method == 'POST':
        messages.success(request,'Thank You for contacting us,we will get back to you sonn')
    return render(request,'page/contact.html')