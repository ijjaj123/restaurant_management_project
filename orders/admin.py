from django.contrib import admin
from .models import UserProfile,Menu,Order

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Menu)
admin.site.register(Order)
