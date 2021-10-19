from django.shortcuts import redirect, render
from django.contrib import messages
from contacts.models import Contact

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        hotel_id = request.POST['hotel_id']
        hotel_name = request.POST['hotel_name']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(hotel_id=hotel_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'You have already made inquiry about this hotel,Please wait until we get back to you.')
                return redirect('/hotels/'+hotel_id)
        
        contact = Contact(hotel_id=hotel_id, hotel_name=hotel_name, user_id=user_id, first_name=first_name,last_name=last_name,
                           customer_need=customer_need, city=city, state=state, email=email, phone=phone, message=message)
        
        contact.save()
        
        messages.success(request,'Your request Has been,we will get back to you shortly.')
        return redirect('/hotels/'+hotel_id)