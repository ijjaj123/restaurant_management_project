from django.shortcuts import render,redirect
from .forms import ContactFrom
import requests




def homepage(request):
    response=requests.get('http://localhost:8000/api/menu-items/')
    menu_items=[]

    if response.status_code==200:
        menu_items=response.json()
    
    if request.method =='POST':
        from=ContactForm(request.POST)
        if from.is_valid():
            from.save()
            return redirect('homepage')
    else:
        from=ContactForm()
    return render(request,'menu/home.html',{
        'menu_items':menu_items,
        'form':form
        
    })


# Create your views here.
