from django import forms
from .models import CustomUser
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['full_name', 'email', 'phone', 'cover_letter', 'resume']

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','password']