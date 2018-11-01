from django import forms
from django.contrib.auth.models import User
from basicapp.models import User_Table

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password')
