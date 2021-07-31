from django import forms
from .models import ContactForm

class FormAddContactForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'contact', 'password']