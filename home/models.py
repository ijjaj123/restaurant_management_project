from django.db import models

# Create your models here.
class RestaurantInfo(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length15)

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