from django.shortcuts import render,redirect
from .forms import ContactForm
import requests
from .models import MenuItem
from django.conf import settings
from .models import RestaurantInfo

def feedback_view(request):
    if request.method=="POST":
        from=FeedbackFrom(request.POST)
        if from.is_valid():
            from.save()
            return redirect("feedback")
    else:
        from=FeedbackFrom()
    return render(request,"home/feedback.html",{"form":form})

def reservations(request):
    try:
        reservation_list=Reservation.objects.all()
        return render(request,'reservations.html',{'reservations':reservation_list})
    except DatabaseError as e:
        print(f"Database error:{e}")
        return render(request,'reservations.html',{
            'error_message':"sorry, We are unable to load reservations at the moment.please try again later."

        })
    except Exception as e:
        print(f"Unexpected error:{e}")
        return render(request,'reservations.html',{
            'error_message': "Something went wrong .please try again later."
        })

def reservations(request):
    return render(request,'reservations.html')

def homepage(request):
    info=RestaurantInfo.objects.first()
    return render(request,'homepage.html',{
        'restaurant_name':info.name if info else"Tasty Bites",
        'phone_number':info.phone if info else "Not Available"
    }) 
def homepage(request):
    return render(request,'homepage.html',{
        'restaurant_name':'Tasty Bites'
    })
def contact_view(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid()
        form.save()
        return redirect("contact")
    else:
        form=ContactForm()
    return render(request,'home/contact.html')

def about_page(request):
    return render(request,'about.html',{
        'restaurant_name':settings.RESTAURANT_NAME
    })
def homepage(request):
    restuarant_name=settings.RESTAURANT_NAME 

    menu_items=[]
    try:
        response=request.get('http://localhost:8000/api/menu-items/')
        if response.status_code==200:
            menu_items=response.json()
        else:
            menu_items=MenuItem.objects.all()
    except:
        menu_items=MenuItem.objects.all()
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            form=ContactForm()
        
        return render(request,'home/homepage.html',{
            'restaurant_name':restaurant_name,
            'menu_items':menu_items,
            'form':form,
        })


# Create your views here.
