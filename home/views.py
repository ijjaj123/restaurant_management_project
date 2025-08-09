from django.shortcuts import render,redirect
from .forms import ContactForm
import requests
from .models import MenuItem
from django.conf import settings

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
