from django import forms
from .models import Contact

class ContactFrom(froms.ModelFrom):
    class Meta:
        model=Contact
        fields=['name','email']