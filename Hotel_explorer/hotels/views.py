from django.shortcuts import get_object_or_404, render
from .models import Hotel
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.
def hotels(request):
    hotels = Hotel.objects.order_by('created_date')
    paginator = Paginator(hotels,4)
    page = request.GET.get('page')
    paged_hotels = paginator.get_page(page)

    city_search = Hotel.objects.values_list('city',flat=True).distinct()

    data = {
        'hotels':paged_hotels,

        'city_search':city_search,

    }
    return render(request,'hotels/hotels.html',data)

def hotel_detail(request,id):
    single_hotel = get_object_or_404(Hotel,pk=id)
    data = {
        'single_hotel':single_hotel,
    }
    return render(request,'hotels/hotel_detail.html',data)

def search(request):
    hotels = Hotel.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            hotels = hotels.filter(hotel_name__icontains=keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            hotels = hotels.filter(city__iexact=city)

    if 'amenity' in request.GET:
        amenity = request.GET['amenity']
        if amenity:
            hotels = hotels.filter(amenities__icontains=amenity)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            hotels =  hotels.filter(price__gte=min_price,price__lte=max_price)

    city_search = Hotel.objects.values_list('city',flat=True).distinct()
    amenity_search = Hotel.objects.values_list('amenities',flat=True)
    x = set()
    for i in amenity_search:
        for j in i:
            x.add(j)
    data = {
        'hotels':hotels,
        'amenities':x,
        'city_search':city_search,
        
    }
    return render(request,'hotels/search.html',data)