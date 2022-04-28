from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Restaurant, Menu, Food


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# from django import forms
# class Customer(forms.ModelForm):
#     class Meta:
#         model = Customer
#         widgets = {
#         'password': forms.PasswordInput(),
#     }        