from django import forms
from .models import Contact
from django.forms import TextInput, EmailInput

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','phone','message']
        widgets ={
            'name':TextInput(
                attrs={
                     "type":"text",
                     "placeholder":"Name"
                }
            ),
             'phone':TextInput(
                attrs={
                     "type":"text",
                     "placeholder":"Phone"
                }
            ),
            'email':EmailInput(
                attrs={
                     "type":"email",
                     "placeholder":"Email"
                }
            ),
            'message':TextInput(
                attrs={
                     "type":"text",
                     "placeholder":"Email",
                     "class":"message-box"
                }
            )
        }