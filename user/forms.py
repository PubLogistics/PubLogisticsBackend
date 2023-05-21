from django import forms
from .models import UserInfo,User

class RegisterForm(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields=('nickname','phone','conductor','company','wage')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password", "email")
