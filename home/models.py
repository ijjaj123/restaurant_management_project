from django.db import models

# Create your models here.
class RestaurantLocation(models.Model):
    address=models.CharField(max_length=255)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.address},{self.city},{self.state} {self.zip_code}"
class RestaurantInfo(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    address=models.TextField(blank=True,null=True)
    opening_hours=models.JSONField(default=dict,blank=True,null=True)
    def __str__(self):
        return self.name
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=150, blank=True)
    message=models.TextField()
    submitted_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    image=models.ImageField(uplod_to="menu_images/",blank=true,null=True)
    def __str__(self):
        return self.name
class Feedback(models.Model):
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback{self.id}-{self.created_at.strftime('%Y-%m-%d %H:%M)}"

class ContactSubmission(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    submitted_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}-{self.email}"