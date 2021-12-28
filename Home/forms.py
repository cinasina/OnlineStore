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
                attrs={"type": "text", "class": "form-control", "name": "name", "id": "name",
                       "placeholder": "Name"}),
            'subject': forms.TextInput(
                attrs={"type": "subject", "class": "form-control", "name": "subject", "id": "subject",
                       "placeholder": "Subject"}),
            'email': forms.EmailInput(
                attrs={"type": "email", "class": "form-control", "name": "email", "id": "email",
                       "placeholder": "Email"}),
            'message': forms.TextInput(
                attrs={"type": "message", "class": "form-control", "name": "message", "id": "message", "cols": "30",
                       "rows": "4", "placeholder": "Message"}),
        }


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'
