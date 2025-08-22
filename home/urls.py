from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('menu/',views.menu_page,name="menu"),
    path('contact/',views.contact_us,name='contact'),
    path('reservations/',views.reservations,name='reservations')  
    path("feedback/",views.feedback_view,name="feedback"),  
    
]