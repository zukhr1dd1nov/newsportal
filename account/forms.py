from django import forms
from re import match
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from django.utils.translation import gettext_lazy as _

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50 , widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    confirm = forms.CharField(max_length=10,required=True,label=_("Parol takroran") ,widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=10,required=True,label=_("Ism"))
    last_name = forms.CharField(max_length=10,required=True,label=_("Famliya"))

    def clean_first_name(self):
        data = str(self.cleaned_data.get('first_name'))
        if not re.match("^[A-Za-z]+$",data):
            raise ValidationError(_("Iltimos faqat lotin harflarinin kiriting!"))

        return data
    
    def clean(self):
        data = super().clean()

        if data.get('password') != data.get('confirm'):
            raise ValidationError(
                {
                    "confirm":_("Parollar bir-xil emas")
                }
            )
        return data


    class Meta:
        model = User
        widgets = {
            'password' : forms.PasswordInput()
        }
        labels = {
            'username' : 'Login',
            "password" : "Parol"
        }
        fields = ('username','first_name','last_name','password')