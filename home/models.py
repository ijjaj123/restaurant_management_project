from django.db import models

# Create your models here.
class RestaurantInfo(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    address=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digit=6,decmial_places=2)

    def __str__(self):
        return self.name
class Feedback(models.Model):
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback{self.id}-{self.created_at.strftime('%Y-%m-%d %H:%M)}"