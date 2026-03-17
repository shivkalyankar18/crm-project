from django import forms

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from .models import Record

from django.contrib.auth.models import User

from django.forms.widgets import PasswordInput,TextInput

from captcha.fields import CaptchaField



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)
    captcha = CaptchaField()



# CREATE A RECORD

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields=['first_name','last_name','email','phone_number','address','city','province','country']

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields=['first_name','last_name','email','phone_number','address','city','province','country']
