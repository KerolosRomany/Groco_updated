import phone_field.forms
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.forms import ModelForm, models
from phone_field import PhoneField

from .models import UserProfile


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'box'}))
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'class': 'box'}))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'box'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'btn-upload'}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class": "box"}))
    mobile = phone_field.forms.PhoneFormField(widget=phone_field.forms.PhoneWidget(attrs={"class": "box"}))

    class Meta:
        model = UserProfile
        fields = ['avatar', 'mobile', 'address']
