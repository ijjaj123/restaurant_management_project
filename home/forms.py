from django import forms
from .models import Contact

class ContactForm(froms.ModelFrom):
    class Meta:
        model=Contact
        fields=['name','email']