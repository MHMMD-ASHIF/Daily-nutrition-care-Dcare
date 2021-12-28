from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
        exclude = ['user']


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


class contactform(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input is-rounded', 'placeholder': 'Enter city name'}))
