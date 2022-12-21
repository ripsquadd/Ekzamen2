from django import forms

from main.models import Service


# from models import Service


class ServiceAddForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('name', 'description', 'image')
        enctype = "multipart/form-data"


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
