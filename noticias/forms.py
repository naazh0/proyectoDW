from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Copropietario
 
 
class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }

class CopropForm(ModelForm):
    class Meta:
        model = Copropietario
        fields = ['name','rut','correo','fono']
