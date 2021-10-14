from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from phonenumber_field.modelfields import PhoneNumberField


class UserCreationForm(forms.ModelForm):
    phone_number = PhoneNumberField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password', 'phone_number')


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = '__all__'
