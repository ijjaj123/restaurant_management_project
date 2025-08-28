from django import forms
from .models import Contact

class ContactForm(froms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email',"subject","message"]
        widgets={
            "name":forms.TextInput(attrs={"class":"input","placheholder":"your name"}),
            "email":forms.EmailInput(attrs={"class":"input","placheholder":"your@example.com"}),
            "subject":forms.TextInput(attrs={"class":"input","placheholder":"subject(optional)"}),
            "message":forms.Textarea(attrs={"class":"textarea","rows":5,"placheholder":"your message"}),
            
        }