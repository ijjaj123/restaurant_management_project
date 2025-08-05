from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15)

    def __str__(slef):
        return slef.name

# Create your models here.
class Order(models.Model):
    ORDER_STATUS_CHOICES=[
        ('PENDING','pending'),
        ('COMPLETED','completed'),
        ('CANCELLED','cancelled'),
    ]
    customer=models.FroeignKey(User,on_delete=models.CASCADE,related_name='orders')
    items=models.ManyToManyField(Menu,related_name='orders')
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=10,choices=ORDER_STATUS_CHOICES,default='PENDING')
    ordered_at=models.DateTimeField(auto_now_add=True)

    def __str__(slef):
        return f"Order #{self.id} by{self.customer.username}"
