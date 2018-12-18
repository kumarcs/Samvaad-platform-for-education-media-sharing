from django import forms
from django.core import validators
from django.contrib.auth.models import User
from basicapp.models import User_Table, Institute, Newsfeed,Comment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = User_Table
        fields = ('access_type',)

class InstituteProfileInfoForm(forms.ModelForm):
    class Meta():
        model = Institute
        fields = {'institute_name','institute_type', 'director'}

class addUserForm(forms.ModelForm):
    class Meta():
        model = User_Table
        fields = {'institute_name_user',}

class addNewsFeedForm(forms.ModelForm):
    class Meta():
        model = Newsfeed
        fields = {'description', 'news_feed_type'}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'user_name', 'description',}
