from django.contrib import admin
from .models import Contact,MenuItem,RestaurantInfo,Feedback

# Register your models here.
admin.site.register(Contact)
@admin,register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display=("name","price","image")
admin.site.register(RestaurantLocation)
