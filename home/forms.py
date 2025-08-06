from django import forms
from .models import Contact

class ContactForm(froms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email']