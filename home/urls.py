from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name='home'),
    path('thank-you/',views.thank_you_view,name='thank_you'),
    
]