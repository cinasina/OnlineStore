from django import forms
from .models import Contact, NewsLetter
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={"type": "text", "class": "input100", "name": "name",
                       "placeholder": "Full Name"}),
            'subject': forms.TextInput(
                attrs={"type": "subject", "class": "input100", "name": "subject",
                       "placeholder": "Subject"}),
            'email': forms.EmailInput(
                attrs={"type": "email", "class": "input100", "name": "email",
                       "placeholder": "E-mail"}),
            'message': forms.TextInput(
                attrs={"type": "message", "class": "input100", "name": "message",
                       "placeholder": "Your Message"}),
        }


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'
