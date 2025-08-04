from requests
from django.shortcuts import render


def homepage(request):
    response=requests.get('http://localhost:8000/api/menu-items/')
    menu_items=[]

    if response.status_code=200:
        menu_items=response.json()
    return render(request,'menu/home.html',{'menu_items':menu_items})


# Create your views here.
