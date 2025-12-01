from django import forms
from .models import Signup_model

class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup_model
        fields = ['username', 'email', 'password', 'confirm_password']
        widget = {
            "password": forms.PasswordInput(),
            "confirm_password": forms.PasswordInput(),
        }



