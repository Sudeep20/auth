from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo,List
from crispy_forms.helper import FormHelper


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')



class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item","completed"]

