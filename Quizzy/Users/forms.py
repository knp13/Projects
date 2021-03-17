from django.contrib.auth import get_user_model
from django import forms
from .models import *

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,
                widget=forms.TextInput(attrs={"placeholder":"Username"}))
    password = forms.CharField(max_length=100,
                widget=forms.PasswordInput(attrs={"placeholder":"Password"}))

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100,
                widget=forms.TextInput(attrs={"placeholder":"Username", "class":"form-control"}))
    email = forms.EmailField(
                widget=forms.TextInput(attrs={"placeholder":"Email", "class":"form-control"}))
    password1 = forms.CharField(label="Password", max_length=100,
                widget=forms.PasswordInput(attrs={"placeholder":"Password", "class":"form-control"}))
    password2 = forms.CharField(label="Confirm Password", max_length=100,
                widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password", "class":"form-control"}))


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
