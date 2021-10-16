from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


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


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': "un", "type": "text", "align": "center", "placeholder": "Email"}))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={"class": "pass", "type": "password", "align": "center",
               "placeholder": "Password"}))


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': "un", "type": "text", "align": "center", "placeholder": "Email"}))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={"class": "pass", "type": "password", "align": "center",
               "placeholder": "Password"}))

    class Meta:
        model = User
        fields = 'phone_number',
        widgets = {'phone_number': PhoneNumberPrefixWidget(
            initial='IR',
            attrs={"class": "pass",
                   "align": "center", "placeholder": "Phone Number"})}
        labels = {'phone_number': ''}
